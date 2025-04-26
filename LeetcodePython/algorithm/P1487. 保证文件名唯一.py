#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 9:53
FileName: algorithm/P1487. 保证文件名唯一.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        index = {}
        for i, name in enumerate(names):
            if name not in index:
                index[name] = 1
            else:
                k = index[name]
                while f'{name}({k})' in index:
                    k += 1
                t = f'{name}({k})'
                names[i] = t
                index[name] = k + 1
                index[t] = 1
        return names


if __name__ == '__main__':
    solution = Solution().getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)"])
    ic(solution)
