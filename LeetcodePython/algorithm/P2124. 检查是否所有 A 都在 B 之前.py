#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 22:10
FileName: P2124. 检查是否所有 A 都在 B 之前
Description:
"""

from icecream import ic


class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s


if __name__ == '__main__':
    solution = Solution().checkString("aaabbb")
    ic(solution)
