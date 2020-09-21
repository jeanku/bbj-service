#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Scripts.BaseScript import BaseScript
from simutil.App import app


class Register(BaseScript):
    uri = '/common/register'

    def run(self):
        param = {
            'account': '18652979331',
            'password': '18652979331',
            'code': '1412',
        }
        data = app('request').post(app('env').DOMAIN + self.uri, params=param, header={}).json()
        code = data.get('retCode', None)
        if code is not None and data.get('retData', {}).get('code', 0) != 404:
            app('log').info(self.uri + ': success, return:' + data.__str__())
        else:
            app('log').error(self.uri + ': error, return:' + data.__str__())


if __name__ == '__main__':
    Register().run()