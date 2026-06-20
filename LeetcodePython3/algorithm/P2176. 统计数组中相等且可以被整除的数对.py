#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:43
FileName: P2176. 统计数组中相等且可以被整除的数对.py
Description:
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:], start=i + 1):
                if num1 == num2 and (i * j) % k == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2)
    print(solution)
