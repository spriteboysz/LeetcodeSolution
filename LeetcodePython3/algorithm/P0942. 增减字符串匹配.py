#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 09:22
FileName: P0942. 增减字符串匹配.py
Description:
"""
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = list(range(len(s) + 1))
        ss = []
        for ch in s:
            if ch == 'I':
                ss.append(nums.pop(0))
            else:
                ss.append(nums.pop())
        ss.append(nums.pop())
        return ss


if __name__ == '__main__':
    solution = Solution().diStringMatch(s="IDID")
    print(solution)
