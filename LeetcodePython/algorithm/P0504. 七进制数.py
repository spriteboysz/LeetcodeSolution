#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 17:41
FileName: P0504. 七进制数
Description:
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = num > 0
        num = abs(num)
        ss = []
        while num:
            num, mod = divmod(num, 7)
            ss.append(mod)
        pref = '-' if not flag else ''
        return pref + ''.join(map(str, ss))[::-1]


if __name__ == '__main__':
    solution = Solution().convertToBase7(num=-101)
    print(solution)
