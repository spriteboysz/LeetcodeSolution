#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 22:48
FileName: P0219. 存在重复元素 II
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(list)
        for i, num in enumerate(nums):
            counter[num].append(i)
        for indexes in counter.values():
            for i in range(1, len(indexes)):
                if indexes[i] - indexes[i - 1] <= k:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(solution)
