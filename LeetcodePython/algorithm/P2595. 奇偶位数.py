#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 12:50
FileName: P2595. 奇偶位数
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        for i, ch in enumerate(bin(n)[2:][::-1]):
            if ch == '0':
                continue
            ans[i % 2] += 1
        return ans


if __name__ == '__main__':
    solution = Solution().evenOddBit(17)
    ic(solution)
