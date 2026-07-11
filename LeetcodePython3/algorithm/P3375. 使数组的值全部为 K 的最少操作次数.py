#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 10:46
FileName: P3375. 使数组的值全部为 K 的最少操作次数.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = {num for num in nums if num != k}
        cnt = 0
        for num in seen:
            if num < k:
                return -1
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minOperations(nums=[5, 2, 5, 4, 5], k=2)
    print(solution)
