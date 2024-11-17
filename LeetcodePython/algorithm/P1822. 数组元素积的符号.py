#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 20:08
FileName: P1822. 数组元素积的符号
Description:
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt0, cnt1 = 0, 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            if num < 0:
                cnt1 += 1
        if cnt0 > 0:
            return 0
        return -1 if cnt1 % 2 == 1 else 1


if __name__ == '__main__':
    solution = Solution().arraySign(nums=[-1, -2, -3, -4, 3, 2, 1])
    print(solution)
