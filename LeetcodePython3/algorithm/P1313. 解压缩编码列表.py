#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:29
FileName: P1313. 解压缩编码列表.py
Description:
"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr, cnt = [], 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                cnt = num
            else:
                arr.extend([num] * cnt)
        return arr


if __name__ == '__main__':
    solution = Solution().decompressRLElist(nums=[1, 2, 3, 4])
    print(solution)
