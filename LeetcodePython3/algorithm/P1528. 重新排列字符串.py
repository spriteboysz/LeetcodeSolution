#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 12:05
FileName: P1528. 重新排列字符串.py
Description:
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [''] * len(s)
        for ch, index in zip(s, indices):
            ss[index] = ch
        return ''.join(ss)

if __name__ == '__main__':
    solution = Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3])
    print(solution)
