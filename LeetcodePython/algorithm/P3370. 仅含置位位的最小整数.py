#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:09
FileName: P3370. 仅含置位位的最小整数
Description:
"""

from icecream import ic


class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(bin(n).replace('0', '1')[2:], 2)


if __name__ == '__main__':
    solution = Solution().smallestNumber(5)
    ic(solution)
