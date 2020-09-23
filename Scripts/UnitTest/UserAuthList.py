#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Scripts.BaseScript import BaseScript
from simutil.App import app
from Scripts.UnitTest.LoginCheck import LoginCheck
from Util.HandyJson import HandyJson


class UserAuthList(BaseScript):
    uri = '/user/auth-list'

    def run(self):
        param = {
            'type': 'draw',
        }
        header = {
            'token': LoginCheck().run()
        }

        data = app('request').post(app('env').DOMAIN + self.uri, params=param, header=header).json()
        data = HandyJson(data)
        code = data.get('retCode', 0)
        if code == 0:
            app('log').info(self.uri + ': success, return:' + data.__str__())
        else:
            app('log').error(self.uri + ': error, return:' + data.__str__())


if __name__ == '__main__':
    UserAuthList().run()
