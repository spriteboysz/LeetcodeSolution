#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-20 23:35
FileName: P0784. 字母大小写全排列.py
Description:
"""
from typing import List
from itertools import product
from collections import deque


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        alpha = [ch for ch in s if ch.isalpha()]
        for el in product(*[[ch.lower(), ch.upper()] for ch in alpha]):
            ans1 = list(s)
            el = deque(el)
            for j, ch in enumerate(s):
                if ch.isalpha():
                    ans1[j] = el.popleft()
            ans.append(''.join(ans1))
        return ans


if __name__ == '__main__':
    solution = Solution().letterCasePermutation(s="a1b2")
    print(solution)
