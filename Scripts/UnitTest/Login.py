#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Scripts.BaseScript import BaseScript
from simutil.App import app
from Util.Aes import Aes
from Util.HandyJson import HandyJson


class Login(BaseScript):
    uri = '/common/login'
    code = None

    def run(self):
        if self.code is None:
            param = {
                'account': app('env')['USER_ACCOUNT'],
                'password': Aes.encrypt(app('env')['USER_PASSWORD'], app('env')['UAES_KEY']),
            }
            data = app('request').post(app('env').DOMAIN + self.uri, params=param, header={}).json()
            self.log(data)
            Login.code = HandyJson(data).get('retData._token', None)
        return self.code


if __name__ == '__main__':
    Login().run()
