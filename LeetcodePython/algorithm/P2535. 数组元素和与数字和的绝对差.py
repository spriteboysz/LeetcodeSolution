#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 23:31
FileName: P2535. 数组元素和与数字和的绝对差
Description:
"""
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum([int(i) for num in nums for i in list(str(num))]) - sum(nums))


if __name__ == '__main__':
    solution = Solution().differenceOfSum(nums=[1, 15, 6, 3])
    print(solution)
