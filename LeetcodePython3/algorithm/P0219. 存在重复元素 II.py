#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 18:23
FileName: P0219. 存在重复元素 II.py
Description:
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i
        return False


if __name__ == '__main__':
    solution = Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    print(solution)
