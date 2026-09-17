#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 16:55
FileName: algorithm/P3527. 找到最常见的回答.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = defaultdict(int)
        for response in responses:
            for word in set(response):
                dic[word] += 1
        return sorted(dic, key=lambda w: (-dic.get(w, 0), w))[0]


if __name__ == '__main__':
    solution = Solution().findCommonResponse(
        responses=[
            ["good", "ok", "good", "ok"],
            ["ok", "bad", "good", "ok", "ok"],
            ["good"], ["bad"]
        ]
    )
    print('<None>' if solution is None else f'{solution=}')
