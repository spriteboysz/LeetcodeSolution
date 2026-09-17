#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 12:51
FileName: algorithm/P1422. 分割字符串的最大得分.py
Description: 
"""


class Solution:
    def maxScore(self, s: str) -> int:
        left, right = 0, s.count('1')
        scores = []
        for c in s[:-1]:
            if c == '0':
                left += 1
            else:
                right -= 1
            scores.append(left + right)
        return max(scores)


if __name__ == '__main__':
    solution = Solution().maxScore(s="011101")
    print('<None>' if solution is None else f'{solution=}')
