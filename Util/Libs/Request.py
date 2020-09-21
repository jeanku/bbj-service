# coding: utf-8
import requests
from requests.adapters import HTTPAdapter
from aiohttp import TCPConnector
import aiohttp


class Request():
    _instance = None

    _retry_time = 0

    _header = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Request, cls).__new__(cls, *args, **kwargs)
            return cls._instance

    def _session(self, retries=0, username=None, password=None):
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        return self.session

    def retry(self, retry_times=0):
        self._retry_time = retry_times
        return self

    def header(self, header={}):
        self._header = header
        return self

    def get(self, url, params={}, timeout=5, username=None, password=None, **kwargs):
        return self._session(self._retry_time, username, password).get(url, params=params, headers=self._header,
                                                                       timeout=timeout, **kwargs)

    def post(self, url, data={}, timeout=5, username=None, password=None, **kwargs):
        return self._session(self._retry_time, username, password).post(url, data=data, headers=self._header,
                                                                        timeout=timeout, **kwargs)

    # 请求网络数据
    async def aiorequest(self, method, url, headers={}, params={}, data={}, username='', password='', **kwargs):
        auth = aiohttp.BasicAuth(login=username, password=password)
        async with aiohttp.ClientSession(headers=headers, auth=auth,
                                         connector=TCPConnector(verify_ssl=False)) as session:
            async with session.__getattribute__(method)(url, params=params, data=data, **kwargs) as response:
                try:
                    return await response.text(), response
                except:
                    return await response.read(), response

    async def aioget(self, url, params={}, headers={}, username='', password='', **kwargs):
        return await self.aiorequest('get', url, params=params, headers=headers, username=username, password=password,
                                     **kwargs)

    async def aiopost(self, url, headers={}, data={}, username='', password='', **kwargs):
        return await self.aiorequest('post', url, data=data, headers=headers, username=username, password=password,
                                     **kwargs)
