#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-25 11:55
FileName: P2496. 数组中字符串的最大值
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if s.isdigit() else len(s) for s in strs)


if __name__ == '__main__':
    solution = Solution().maximumValue(strs=["alic3", "bob", "3", "4", "00000"])
    ic(solution)
