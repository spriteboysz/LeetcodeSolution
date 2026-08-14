#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-11 23:01
FileName: P1861. 旋转盒子.py
Description:
"""
from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for i, row in enumerate(boxGrid):
            s = ''.join(row).split('*')
            for j, ss in enumerate(s):
                s[j] = ''.join(sorted(ss, reverse=True))
            boxGrid[i] = list('*'.join(s))
        return [list(row) for row in zip(*boxGrid[::-1])]


if __name__ == '__main__':
    solution = Solution().rotateTheBox(
        [['#', '#', '*', '.', '*', '.'],
         ['#', '#', '#', '*', '.', '.'],
         ['#', '#', '#', '.', '#', '.']]
    )
    print(solution)
