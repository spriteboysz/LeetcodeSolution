#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 21:58
FileName: LCP 50. 宝石补给
Description:
"""
from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            cnt = gem[x] // 2
            gem[x] -= cnt
            gem[y] += cnt
        return max(gem) - min(gem)


if __name__ == '__main__':
    solution = Solution().giveGem(gem=[3, 1, 2], operations=[[0, 2], [2, 1], [2, 0]])
    print(solution)
