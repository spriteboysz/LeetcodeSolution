#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-07 22:33
FileName: P3674. 数组元素相等的最小操作次数.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return int(len(set(nums)) != 1)


if __name__ == '__main__':
    s = Solution().minOperations([1, 2, 3, 4])
    print(s)
    import time
    for i in range(100):
        time.sleep(1)
        print(i)
