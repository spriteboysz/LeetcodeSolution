#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 22:14
FileName: LCP 72. 补给马车
Description:
"""
from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        m = len(supplies) // 2
        while (n := len(supplies)) > m:
            index = 1
            for i in range(1, n):
                if supplies[i - 1] + supplies[i] < supplies[index - 1] + supplies[index]:
                    index = i
            supplies[index - 1] += supplies[index]
            supplies.pop(index)
        return supplies


if __name__ == '__main__':
    solution = Solution().supplyWagon(supplies=[7, 3, 6, 1, 8])
    print(solution)
