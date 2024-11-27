#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:22
FileName: P2367. 等差三元组的数目
Description:
"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        for k, num3 in enumerate(nums):
            for j, num2 in enumerate(nums[:k]):
                if num3 - num2 != diff:
                    continue
                for num1 in nums[:j]:
                    if num2 - num1 == diff:
                        cnt += 1
                        break
        return cnt


if __name__ == '__main__':
    solution = Solution().arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3)
    print(solution)
