#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-28 21:18
FileName: algorithm/P2379. 得到 K 个黑块的最少涂色次数.py
Description: 
"""

from icecream import ic


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return min(blocks[i - k:i].count('W') for i in range(k, len(blocks) + 1))


if __name__ == '__main__':
    solution = Solution().minimumRecolors(blocks="WBBWWBBWBW", k=7)
    ic(solution)
