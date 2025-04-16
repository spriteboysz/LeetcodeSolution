#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-16 21:46
FileName: algorithm/P2611. 老鼠和奶酪.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = [num1 - num2 for num1, num2 in zip(reward1, reward2)]
        diff.sort(reverse=True)
        return sum(reward2) + sum(diff[:k])


if __name__ == '__main__':
    solution = Solution().miceAndCheese(reward1=[1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2)
    ic(solution)
