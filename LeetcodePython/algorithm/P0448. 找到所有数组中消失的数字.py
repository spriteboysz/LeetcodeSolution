#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 23:14
FileName: P0448. 找到所有数组中消失的数字
Description:
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        return [num + 1 for num in range(len(nums)) if num + 1 not in seen]


if __name__ == '__main__':
    solution = Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1])
    print(solution)
