#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:32
FileName: P2525. 根据规则将箱子分类.py
Description:
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        flag1, flag2 = False, False
        if max(length, width, height) >= 10 ** 4 or length * width * height >= 10 ** 9:
            flag1 = True
        if mass >= 100:
            flag2 = True
        if flag1 and flag2:
            return 'Both'
        if flag1:
            return 'Bulky'
        if flag2:
            return 'Heavy'
        return 'Neither'


if __name__ == '__main__':
    solution = Solution().categorizeBox(length=1000, width=35, height=700, mass=300)
    print(solution)
