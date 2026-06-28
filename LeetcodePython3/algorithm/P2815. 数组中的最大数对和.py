#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 12:31
FileName: P2815. 数组中的最大数对和.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for num in nums:
            dic[max(int(digit) for digit in str(num))].append(num)
        return max((sum(sorted(v)[-2:]) for v in dic.values() if len(v) >= 2), default=-1)


if __name__ == '__main__':
    solution = Solution().maxSum(nums=[51, 71, 17, 24, 42])
    print(solution)
