#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""list处理类"""


class List():

    @staticmethod
    def sum(data: list):
        count = 0
        for i in data:
            assert isinstance(i, int) or isinstance(i, float), 'Element does not meet the requirements'
            count += i
        return count



if __name__ == '__main__':
    print(List.sum([1,2,3,4]))
