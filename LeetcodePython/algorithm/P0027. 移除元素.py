#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 16:59
FileName: P0027. 移除元素
Description:
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == '__main__':
    solution = Solution().removeElement(nums=[3, 2, 2, 3], val=3)
    print(solution)
