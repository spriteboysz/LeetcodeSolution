#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-12-14 23:11
FileName: P3712. 出现次数能被 K 整除的元素总和.py
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return sum(num * count for num, count in dic.items() if count % k == 0)


if __name__ == '__main__':
    s = Solution().sumDivisibleByK(nums=[1, 2, 2, 3, 3, 3, 3, 4], k=2)
    print(s)
