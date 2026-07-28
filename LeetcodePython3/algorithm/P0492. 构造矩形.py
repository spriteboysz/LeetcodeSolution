#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-27 23:08
FileName: P0492. 构造矩形.py
Description:
"""
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5) + 1, 0, -1):
            if area % i == 0:
                return sorted([area // i, i], reverse=True)
        return [area, 1]


if __name__ == '__main__':
    solution = Solution().constructRectangle(122122)
    print(solution)
