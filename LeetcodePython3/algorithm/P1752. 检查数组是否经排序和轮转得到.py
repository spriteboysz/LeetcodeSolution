#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:01
FileName: P1752. 检查数组是否经排序和轮转得到.py
Description:
"""
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        return '#'.join(map(str, sorted(nums))) in '#'.join(map(str, nums * 2))


if __name__ == '__main__':
    solution = Solution().check(nums=[3, 4, 5, 1, 2])
    print(solution)
