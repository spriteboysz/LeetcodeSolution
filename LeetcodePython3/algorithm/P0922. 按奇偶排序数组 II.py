#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 10:48
FileName: P0922. 按奇偶排序数组 II.py
Description:
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        nums[::2], nums[1::2] = even, odd
        return nums


if __name__ == '__main__':
    solution = Solution().sortArrayByParityII([1, 2, 3, 4])
    print(solution)
