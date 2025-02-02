#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 22:38
FileName: P2710. 移除字符串中的尾随零
Description:
"""

from icecream import ic


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


if __name__ == '__main__':
    solution = Solution().removeTrailingZeros(num="51230100")
    ic(solution)
