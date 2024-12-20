#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 22:23
FileName: LCP 77. 符文储备
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        counter = Counter(runes)

        nums = sorted(list(counter))
        maximum, curr = 0, counter.get(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] <= 1:
                curr += counter.get(nums[i])
            else:
                maximum = max(maximum, curr)
                curr = counter.get(nums[i])
        return max(maximum, curr)


if __name__ == '__main__':
    solution = Solution().runeReserve(runes=[1, 1, 3, 3, 4])
    print(solution)
