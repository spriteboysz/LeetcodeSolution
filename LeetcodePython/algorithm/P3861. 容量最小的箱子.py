#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-03-15 11:51
FileName: P3861. 容量最小的箱子.py
Description:
"""


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        return min([(c, i) for i, c in enumerate(capacity) if c >= itemSize], default=(None, -1))[1]


if __name__ == '__main__':
    s = Solution().minimumIndex(capacity=[1, 5, 3, 7], itemSize=100)
    print(s)
