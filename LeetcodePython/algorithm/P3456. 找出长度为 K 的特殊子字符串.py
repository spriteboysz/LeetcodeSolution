#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-17 23:02
FileName: algorithm/P3456. 找出长度为 K 的特殊子字符串.py
Description: 
"""

from icecream import ic


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        nums = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                nums.append(nums[-1] + 1)
                nums[-2] = -1
            else:
                nums.append(1)
        return k in nums


if __name__ == '__main__':
    solution = Solution().hasSpecialSubstring(s="ccc", k=2)
    ic(solution)
