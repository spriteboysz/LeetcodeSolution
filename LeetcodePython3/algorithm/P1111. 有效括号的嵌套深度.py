#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-10 22:49
FileName: P1111. 有效括号的嵌套深度.py
Description:
"""
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depths, depth = [], 0
        for c in seq:
            if c == '(':
                depth += 1
                depths.append(depth % 2)
            else:
                depths.append(depth % 2)
                depth -= 1
        return depths


if __name__ == '__main__':
    solution = Solution().maxDepthAfterSplit(seq="(()())")
    print(solution)
