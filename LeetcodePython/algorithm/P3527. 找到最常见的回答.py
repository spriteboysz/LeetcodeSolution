#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-25 09:42
FileName: algorithm/P3527. 找到最常见的回答.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = defaultdict(int)
        for response in responses:
            response = set(response)
            for resp in response:
                dic[resp] += 1
        maximum = max(dic.values())
        return min([k for k, v in dic.items() if v == maximum])


if __name__ == '__main__':
    solution = Solution().findCommonResponse(
        responses=[["good", "ok", "good", "ok"], ["ok", "bad", "good", "ok", "ok"], ["good"], ["bad"]])
    ic(solution)
