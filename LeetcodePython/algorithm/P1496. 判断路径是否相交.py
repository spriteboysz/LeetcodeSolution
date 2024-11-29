#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 23:35
FileName: P1496. 判断路径是否相交
Description:
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        x, y = 0, 0
        points = {(x, y)}
        for direction in path:
            dx, dy = directions.get(direction)
            x, y = x + dx, y + dy
            if (x, y) in points:
                return True
            points.add((x, y))
        return False


if __name__ == '__main__':
    solution = Solution().isPathCrossing(path="NESWW")
    print(solution)
