#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-01 10:01
FileName: P1694. 重新格式化电话号码
Description:
"""

from icecream import ic


class Solution:
    def reformatNumber(self, number: str) -> str:
        ss = []
        for i, ch in enumerate(filter(lambda el: el.isdigit(), number), start=1):
            ss.append(ch)
            if i % 3 == 0:
                ss.append('-')
        if len(ss) < 2:
            raise ValueError('Error')
        if ss[-2] == '-':
            ss[-2], ss[-3] = ss[-3], ss[-2]
        return ''.join(ss).strip('-')


if __name__ == '__main__':
    solution = Solution().reformatNumber(number="123 4-567")
    ic(solution)
