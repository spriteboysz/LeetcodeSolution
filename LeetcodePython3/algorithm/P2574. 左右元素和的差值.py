#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-09 23:20
FileName: P2574. 左右元素和的差值.py
Description:
"""
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        def calc(arr: List):
            acc, ans = 0, []
            for num in arr:
                ans.append(acc)
                acc += num
            return ans

        return [abs(num1 - num2) for num1, num2 in zip(calc(nums), calc(nums[::-1])[::-1])]


if __name__ == '__main__':
    solution = Solution().leftRightDifference(nums=[10, 4, 8, 3])
    print(solution)
