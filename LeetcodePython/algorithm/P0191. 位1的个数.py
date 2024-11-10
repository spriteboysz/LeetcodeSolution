#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:33
FileName: P0191. 位1的个数
Description:
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


if __name__ == '__main__':
    solution = Solution().hammingWeight(11)
    print(solution)
