#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 22:33
FileName: P1528. 重新排列字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [''] * len(s)
        for ch, i in zip(s, indices):
            ss[i] = ch
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
    ic(solution)
