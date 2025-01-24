#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-18 16:32
FileName: P1433. 检查一个字符串是否可以打破另一个字符串
Description:
"""

from icecream import ic


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ss1, ss2 = sorted(s1), sorted(s2)
        result1 = [ch1 <= ch2 for ch1, ch2 in zip(ss1, ss2)]
        result2 = [ch1 >= ch2 for ch1, ch2 in zip(ss1, ss2)]
        return all(result1) or all(result2)


if __name__ == '__main__':
    solution = Solution().checkIfCanBreak(s1="yopumzgd", s2="pamntyya")
    ic(solution)
