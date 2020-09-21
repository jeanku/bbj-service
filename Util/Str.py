#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = ''


class Str(object):

    @staticmethod
    def md5(str):
        import hashlib
        return hashlib.md5(str.__str__().encode(encoding='UTF-8')).hexdigest()
