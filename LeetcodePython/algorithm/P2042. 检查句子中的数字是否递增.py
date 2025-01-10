#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-09 23:37
FileName: P2042. 检查句子中的数字是否递增
Description:
"""
import re

from icecream import ic


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int, re.findall(r'(\d+)', s)))
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    ic(solution)
