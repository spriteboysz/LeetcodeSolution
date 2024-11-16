#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:46
FileName: P2357. 使数组中所有元素都等于零
Description:
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num})


if __name__ == '__main__':
    solution = Solution().minimumOperations(nums=[1, 5, 0, 3, 5])
    print(solution)
