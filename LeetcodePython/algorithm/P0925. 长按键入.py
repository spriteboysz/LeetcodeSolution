#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 21:49
FileName: P0925. 长按键入
Description:
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        m, n = len(name), len(typed)

        while j < n:
            if i < m and j < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j >= 1 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == m


if __name__ == '__main__':
    solution = Solution().isLongPressedName(name="alex", typed="aaleexx")
    print(solution)
