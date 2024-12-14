#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:44
FileName: LCR 169. 招式拆解 II
Description:
"""
from collections import Counter


class Solution:
    def dismantlingAction(self, arr: str) -> str:
        counter = Counter(arr)
        for ch in arr:
            if counter.get(ch) == 1:
                return ch
        return ' '


if __name__ == '__main__':
    solution = Solution().dismantlingAction("abbccdeff")
    print(solution)
