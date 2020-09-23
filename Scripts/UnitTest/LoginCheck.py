#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Scripts.BaseScript import BaseScript
from simutil.App import app
from Scripts.UnitTest.Login import Login
from Util.HandyJson import HandyJson


class LoginCheck(BaseScript):
    uri = '/common/login-check'
    # token = 'NJ6IzMJxWbfVeZKL5mD4e52+T+Pv0xtxFNq1vsrKH8ZtIx3SZ6anjVdYoaHXFYjhv/hgLG0MetRLq75muT8FSw=='
    token = None

    def run(self):
        if self.token is None:
            param = {
                '_token': Login().run(),
                'phone_code': '1314',
                'email_code': '1314',
                'google_code': '1314',
            }
            data = app('request').post(app('env').DOMAIN + self.uri, params=param, header={}).json()
            hjdata = HandyJson(data)
            self.token = hjdata.get('retData.token', None)
            if self.token is None:
                app('log').error(self.uri + ': error, return:' + hjdata.__str__())
            else:
                app('log').info(self.uri + ': success, return:' + hjdata.__str__())
        return self.token


if __name__ == '__main__':
    token = LoginCheck().run()
