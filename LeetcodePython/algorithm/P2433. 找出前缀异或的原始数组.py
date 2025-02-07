#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-07 21:09
FileName: P2433. 找出前缀异或的原始数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        nums = [pref[0]]
        for i in range(1, len(pref)):
            nums.append(pref[i] ^ pref[i - 1])
        return nums


if __name__ == '__main__':
    solution = Solution().findArray(pref=[5, 2, 0, 3, 1])
    ic(solution)
