#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 10:20
FileName: LCR 133. 位 1 的个数
Description:
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

if __name__ == '__main__':
    solution = Solution().hammingWeight(n = 4294967293)
    print(solution)