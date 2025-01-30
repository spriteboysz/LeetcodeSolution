#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:28
FileName: P3340. 检查平衡字符串
Description:
"""

from icecream import ic


class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(map(int, num[::2])) == sum(map(int, num[1::2]))


if __name__ == '__main__':
    solution = Solution().isBalanced(num="24123")
    ic(solution)
