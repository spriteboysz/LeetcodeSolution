#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-10 22:31
FileName: P1496. 判断路径是否相交.py
Description:
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen = {(x, y)}
        for direction in path:
            if direction == 'N':
                y += 1
            if direction == 'S':
                y -= 1
            if direction == 'W':
                x -= 1
            if direction == 'E':
                x += 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False


if __name__ == '__main__':
    solution = Solution().isPathCrossing(path="NESWW")
    print(solution)
