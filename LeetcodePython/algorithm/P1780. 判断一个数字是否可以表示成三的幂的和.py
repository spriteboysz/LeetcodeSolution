#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 22:02
FileName: P1780. 判断一个数字是否可以表示成三的幂的和
Description:
"""

from icecream import ic


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            n, mod = divmod(n, 3)
            if mod > 1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().checkPowersOfThree(21)
    ic(solution)
