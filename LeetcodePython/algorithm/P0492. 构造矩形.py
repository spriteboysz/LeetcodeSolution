#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 22:08
FileName: P0492. 构造矩形
Description:
"""
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [i, area // i]
        return [0, 0]


if __name__ == '__main__':
    solution = Solution().constructRectangle(4)
    print(solution)
