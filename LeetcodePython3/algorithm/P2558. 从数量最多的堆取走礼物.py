#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-23 22:52
FileName: P2558. 从数量最多的堆取走礼物.py
Description:
"""
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts.sort()
            gifts[-1] = math.floor(gifts[-1] ** 0.5)
            k -= 1
        return sum(gifts)


if __name__ == '__main__':
    solution = Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4)
    print(solution)
