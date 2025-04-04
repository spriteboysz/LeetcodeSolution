#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 9:29
FileName: LCP/LCP 18. 早餐组合.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort(reverse=True)
        left, right, cnt = 0, 0, 0
        while left < len(staple) and right < len(drinks):
            if staple[left] > x:
                break
            if staple[left] + drinks[right] <= x:
                cnt += len(drinks) - right
                left += 1
            else:
                right += 1
        return cnt % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().breakfastNumber(staple=[10, 20, 5], drinks=[5, 5, 2], x=15)
    ic(solution)
