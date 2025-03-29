#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-29 22:59
FileName: algorithm/P2739. 总行驶距离.py
Description: 
"""

from icecream import ic


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        cnt = 0
        while mainTank >= 5:
            cnt += 10 * 5
            mainTank -= 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        return cnt + mainTank * 10


if __name__ == '__main__':
    solution = Solution().distanceTraveled(mainTank=5, additionalTank=10)
    ic(solution)
