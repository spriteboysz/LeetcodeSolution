#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-19 22:52
FileName: P2023. 连接后等于目标字符串的字符串对
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = 0
        for i, ch1 in enumerate(nums):
            for j, ch2 in enumerate(nums):
                if i == j:
                    continue
                if ch1 + ch2 == target:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numOfPairs(nums=["777", "7", "77", "77"], target="7777")
    ic(solution)
