#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 11:18
FileName: P0830. 较大分组的位置
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        s += ' '
        res = []
        p1, p2 = 0, 0
        s = s + ' '

        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                continue
            p2 = i
            if p2 - p1 >= 2:
                res.append([p1, p2])
            p1 = i + 1
        return res


if __name__ == '__main__':
    solution = Solution().largeGroupPositions("abcdddeeeeaabbbcd")
    ic(solution)
