#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 11:57
FileName: P0925. 长按键入.py
Description:
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j > 0 and typed[j - 1] == typed[j]:
                    j += 1
                else:
                    return False
        return i == len(name)


if __name__ == '__main__':
    solution = Solution().isLongPressedName(name="vtkgn", typed="vttkgnn")
    print(solution)
