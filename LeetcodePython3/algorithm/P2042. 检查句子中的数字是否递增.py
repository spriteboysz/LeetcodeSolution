#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:38
FileName: P2042. 检查句子中的数字是否递增.py
Description:
"""
from itertools import pairwise


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(word) for word in s.strip().split() if word.isdigit()]
        return all(num1 < num2 for num1, num2 in pairwise(nums))


if __name__ == '__main__':
    solution = Solution().areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    print(solution)
