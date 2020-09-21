# -*- coding: UTF-8 -*-

import logging, requests, json
import datetime
from datetime import datetime
from Util.Libs.Env import Env
from Util.Libs.Redis import Redis

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=Env().storage_path + 'wechat.log',
                    filemode='w')
logger = logging.getLogger('wechat')


class WechatCorpHandler():
    def __init__(self, touser, agentid, corpid, secret):
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        self.__touser = touser
        self.__agentid = agentid
        self.__corpid = corpid
        self.__secret = secret
        self.redis_key = 'lh:wechart:token'

    def __get_token(self, corpid, secret):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {"corpid": corpid, "corpsecret": secret}
        token = Redis.get(self.redis_key)
        if token:
            return str(token, 'utf-8')
        else:
            try:
                r = requests.get(url=url, params=data, verify=True)
                token = r.json()['access_token']
                expires_in = r.json()['expires_in']
                Redis.set(self.redis_key, token)
                Redis.expire(self.redis_key, expires_in)
                return token
            except Exception as E:
                logging.error(E)

    def send(self, msg):
        token = self.__get_token(self.__corpid, self.__secret)
        req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)

        d = {
            'touser': self.__touser,
            'msgtype': 'text',
            'agentid': self.__agentid,
            'text': {
                'content': msg
            },
            'safe': '0'
        }
        # symbol = hashlib.md5((msg).encode('utf-8')).hexdigest()
        requests.post(url=req_url, data=json.dumps(d), verify=False)

    def upload(self, path):
        token = self.__get_token(self.__corpid, self.__secret)
        req_url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload'
        param = {'access_token': token, 'type': 'image'}
        d = {'media': open(path, 'rb')}
        r = requests.post(url=req_url, params=param, files=d)
        res = r.json()
        return res['media_id']

    def send_pic(self, media_id):
        token = self.__get_token(self.__corpid, self.__secret)
        # req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)
        req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)
        d = {
            'touser': self.__touser,
            'msgtype': 'image',
            'agentid': self.__agentid,
            'image': {
                'media_id': media_id
            },
            'safe': '0'
        }
        # symbol = hashlib.md5((msg).encode('utf-8')).hexdigest()
        requests.post(url=req_url, data=json.dumps(d), verify=False)
        # r = requests.post(url = req_url, params = param , data = json.dumps(d), verify = False)
        # logger.info(json.dumps(r.json()))


class WechatHandler():
    def __init__(self, appid, secret):
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        self.__appid = appid
        self.__secret = secret

    def __get_token(self, appid, secret):
        token_file = '/tmp/.{}.token.id'.format(appid)
        try:
            with open(token_file, mode='r') as f:
                obj = json.loads(f.read())
                ts = datetime.strptime(obj['update_ts'], '%Y%m%d%H%M%S')
                time_delta = (datetime.now() - ts).total_seconds()
                if time_delta < 3600 and obj['secret'] == secret:
                    return obj['token']
        except Exception as e:
            pass

        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {"appid": appid, "secret": secret, "grant_type": "client_credential"}
        r = requests.get(url=url, params=data, verify=False)
        logger.info(json.dumps(r.json()))
        token = r.json()['access_token']
        with open(token_file, mode='w') as f:
            f.write(json.dumps({
                'token': token, 'secret': secret,
                'update_ts': datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
            }))
        return token

    def send(self, msg):
        token = self.__get_token(self.__appid, self.__secret)
        # req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)
        req_url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send'
        param = {'access_token': token}
        d = {
            'msgtype': 'text',
            'appid': self.__appid,
            'text': {
                'content': msg
            },
            'safe': '0'
        }
        # symbol = hashlib.md5((msg).encode('utf-8')).hexdigest()
        r = requests.post(url=req_url, params=param, data=json.dumps(d), verify=False)
        print(r)
        logger.info(json.dumps(r.json()))


def test_pic_send(h, mid):
    h.send_pic(mid)


def test_pic_upload(h):
    # h.upload('/tmp/pic.jpg')
    h.upload('screen.png')


if __name__ == '__main__':
    # https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx5114007c5499ae1b&secret=da83f0a8b5e339055bc3ea13406005b6
    # handler = CybexWechatHandler('wx5114007c5499ae1b', 'da83f0a8b5e339055bc3ea13406005b6')
    # handler = CybexWechatCorpHandler('@all',1000020,'ww128a164565b145a8','pAuquvqrJY2-LLjMq8_6I9EpdbXzOCZ5OatQNjXggQ8')
    handler = WechatCorpHandler(env.WARN_TOUSER, env.WARN_AGENTID, env.WARN_CORPID, env.WARN_SECRET)
    # handler = CybexWechatCorpHandler('@all',1000007,'ww128a164565b145a8','-Fi5taTjGx0BlEv36M3HIwOWgtMKCP2LlywrbD9FcSU')
    # handler.send('this is a test from sunxiaoqi!')
    # mid = test_pic_upload(handler)
    # mid = '3L6D-hPH9uKjB89iTf-HZ-c_qvqyVjYeouSr_6LtSWxSrEy168yj3qciuZmn5V_4D'
    # mid = '3JcoIe7uBDgiYUH63pK_t1IR4as1AgQrpp_7U6AGeFPOy3RJ6LBLWFg-Q05VYsWgC'
    # test_pic_send(handler, mid)
    handler.send('hello!')
