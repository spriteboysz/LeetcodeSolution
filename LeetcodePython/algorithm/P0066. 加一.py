#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:54
FileName: P0066. 加一
Description:
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums, carry = [], 1
        for digit in digits[::-1]:
            carry, mod = divmod(carry + digit, 10)
            nums.append(mod)
        if carry:
            nums.append(carry)
        return nums[::-1]


if __name__ == '__main__':
    solution = Solution().plusOne([9, 9])
    print(solution)
