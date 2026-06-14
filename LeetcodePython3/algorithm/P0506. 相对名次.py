#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 15:06
FileName: P0506. 相对名次.py
Description:
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal', *[str(el + 1) for el in range(3, len(score))]]
        dic = {k: i for i, k in enumerate(sorted(score, reverse=True))}
        return [ranks[dic.get(num, 0)] for num in score]


if __name__ == '__main__':
    solution = Solution().findRelativeRanks(score=[5, 4, 3, 2, 1])
    print(solution)
