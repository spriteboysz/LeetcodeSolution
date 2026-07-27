#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-26 21:40
FileName: P0830. 较大分组的位置.py
Description:
"""
from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups = []
        left, right = 0, 0
        s += '#'
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                right = i
            else:
                if right - left >= 2:
                    groups.append([left, right])
                left = right = i
        return groups


if __name__ == '__main__':
    solution = Solution().largeGroupPositions("abcdddeeeeaabbbcddd")
    print(solution)
