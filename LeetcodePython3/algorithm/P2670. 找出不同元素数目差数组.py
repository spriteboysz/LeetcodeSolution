#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 15:33
FileName: P2670. 找出不同元素数目差数组.py
Description:
"""
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        counter1, counter2, seen = [], [0], set()
        for num in nums:
            seen.add(num)
            counter1.append(len(seen))
        seen.clear()
        for num in nums[::-1][:-1]:
            seen.add(num)
            counter2.append(len(seen))

        return [cnt1 - cnt2 for cnt1, cnt2 in zip(counter1, counter2[::-1])]


if __name__ == '__main__':
    solution = Solution().distinctDifferenceArray(nums=[37, 37, 37, 37, 33])
    print(solution)
