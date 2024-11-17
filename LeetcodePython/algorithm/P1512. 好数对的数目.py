#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 21:41
FileName: P1512. 好数对的数目
Description:
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[:i]:
                if num1 == num2:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3])
    print(solution)
