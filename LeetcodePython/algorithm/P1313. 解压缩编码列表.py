#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 10:09
FileName: P1313. 解压缩编码列表
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i in range(0, len(nums), 2):
            decompress.extend([nums[i + 1]] * nums[i])
        return decompress


if __name__ == '__main__':
    solution = Solution().decompressRLElist([1, 2, 3, 4])
    ic(solution)
