#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-21 22:13
FileName: algorithm/P1652. 拆炸弹.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    ans[i] += code[j % n]
            else:
                for j in range(i + k, i):
                    ans[i] += code[(j + n) % n]
        return ans


if __name__ == '__main__':
    solution = Solution().decrypt(code=[5, 7, 1, 4], k=3)
    ic(solution)
