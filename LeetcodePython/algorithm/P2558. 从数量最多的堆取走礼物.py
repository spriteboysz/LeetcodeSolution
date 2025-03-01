#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-01 16:41
FileName: P2558. 从数量最多的堆取走礼物
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            k -= 1
            gifts.sort(reverse=True)
            gifts[0] = int(gifts[0] ** 0.5)
        return sum(gifts)


if __name__ == '__main__':
    solution = Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4)
    ic(solution)
