#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""crontab 解析类"""

import re


class Parser(object):

    def parse(self, now, cron):
        crons = cron.split()
        if crons.__len__() != 6:
            raise Exception('crontab invalid exception : {}'.format(cron))
        return (self.check(now.second, crons[0]) and self.check(now.minute, crons[1]) and self.check(now.hour, crons[2])
                and self.check(now.day, crons[3]) and self.check(now.month, crons[4]) and self.check(now.weekday(),
                                                                                                     crons[5]))

    def check(self, value, item):
        if item == '*':
            return True
        return self.deal_item(value, item)

    def deal_item(self, value, item):
        pattern = re.match("\*/(\d*)", item)
        if pattern:
            return value % int(pattern[1]) == 0

        if item.isnumeric():
            return value == int(item)

        pattern = re.match("^(\d*)-(\d*)$", item)
        if pattern:
            return value in self.deal_underline(pattern.groups(), 1)

        pattern = re.match("(\d*)-(\d*)/(\d*)", item)
        if pattern:
            return value in self.deal_underline(pattern.groups(), int(pattern.groups()[2]))

        if ',' in item:
            return value in self.deal_comma(item)

        return False

    def deal_comma(self, item):
        pattern = item.split(',')
        result = list()
        for i in pattern:
            if i.isnumeric():
                result.append(int(i))
            elif re.match("^(\d*)-(\d*)$", i):
                List_item = re.match("^(\d*)-(\d*)$", i).groups()
                result.extend(self.deal_underline(List_item, 1))
            elif re.match("(\d*)-(\d*)/(\d*)", i):
                List_item = re.match("(\d*)-(\d*)/(\d*)", i).groups()
                result.extend(self.deal_underline(List_item, int(List_item[2])))
            # elif
        return result

    def deal_underline(self, List, divisor):
        start = int(List[0])
        end = int(List[1])
        if start > end:
            return self.deal_divisor(list(range(start, 61)) + list(range(0, end + 1)), divisor)
        elif start < end:
            return self.deal_divisor(list(range(start, end + 1)), divisor)
        else:
            return [start]

    def deal_divisor(self, List, divisor):
        return [i for i in List if i % divisor == 0]
