#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:08
FileName: P3226. 使两个整数相等的位更改次数
Description:
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return -1 if n & k != k else (n ^ k).bit_count()


if __name__ == '__main__':
    solution = Solution().minChanges(13, 14)
    print(solution)
