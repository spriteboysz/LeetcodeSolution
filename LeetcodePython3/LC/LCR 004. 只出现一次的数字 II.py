#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 13:54
FileName: LC/LCR 004. 只出现一次的数字 II.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return [num for num, cnt in dic.items() if cnt == 1][0]


if __name__ == '__main__':
    solution = Solution().singleNumber([2, 2, 3, 2])
    print(solution)
