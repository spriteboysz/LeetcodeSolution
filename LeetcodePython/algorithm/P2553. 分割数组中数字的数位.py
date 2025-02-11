#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-10 23:17
FileName: P2553. 分割数组中数字的数位
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        separate = []
        for num in nums:
            separate.extend(map(int, list(str(num))))
        return separate


if __name__ == '__main__':
    solution = Solution().separateDigits(nums=[13, 25, 83, 77])
    ic(solution)
