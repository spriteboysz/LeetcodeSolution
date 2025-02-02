#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 12:55
FileName: P2525. 根据规则将箱子分类
Description:
"""

from icecream import ic


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky, heavy = False, False
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
            bulky = True
        if mass >= 100:
            heavy = True
        if bulky and heavy:
            return 'Both'
        if bulky:
            return 'Bulky'
        if heavy:
            return 'Heavy'
        return 'Neither'


if __name__ == '__main__':
    solution = Solution().categorizeBox(length=1000, width=35, height=700, mass=300)
    ic(solution)
