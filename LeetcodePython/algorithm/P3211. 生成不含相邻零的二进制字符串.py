#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-03 21:02
FileName: P3211. 生成不含相邻零的二进制字符串
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ss = []
        for i in range(2 ** n):
            v = bin(i)[2:].zfill(n)
            if '00' not in v:
                ss.append(v)
        return ss


if __name__ == '__main__':
    solution = Solution().validStrings(3)
    ic(solution)
