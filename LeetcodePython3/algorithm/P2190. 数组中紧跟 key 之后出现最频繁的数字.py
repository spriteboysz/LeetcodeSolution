#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-21 19:37
FileName: P2190. 数组中紧跟 key 之后出现最频繁的数字.py
Description:
"""
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dic = defaultdict(int)
        for num1, num2 in pairwise(nums):
            if num1 == key:
                dic[num2] += 1
        maximum = max(dic.values())
        return [k for k, v in dic.items() if v == maximum][0]


if __name__ == '__main__':
    solution = Solution().mostFrequent(nums=[1, 100, 200, 1, 100], key=1)
    print(solution)
