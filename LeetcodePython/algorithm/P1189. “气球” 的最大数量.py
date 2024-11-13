#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-12 23:34
FileName: P1189. “气球” 的最大数量
Description:
"""
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(
            counter.get('b', 0),
            counter.get('a', 0),
            counter.get('l', 0) // 2,
            counter.get('o', 0) // 2,
            counter.get('n', 0))


if __name__ == '__main__':
    solution = Solution().maxNumberOfBalloons(text="loonbalxballpoon")
    print(solution)
