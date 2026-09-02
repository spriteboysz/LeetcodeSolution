#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 09:05
FileName: algorithm/P2917. 找出数组中的 K-or 值.py
Description: 
"""
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ss = [bin(num)[2:].zfill(32) for num in nums]
        ans = []
        for bits in zip(*ss):
            ans.append(int(bits.count('1') >= k))
        return int(''.join(map(str, ans)), 2)


if __name__ == '__main__':
    solution = Solution().findKOr(nums=[7, 12, 9, 8, 9, 15], k=4)
    print(solution)
