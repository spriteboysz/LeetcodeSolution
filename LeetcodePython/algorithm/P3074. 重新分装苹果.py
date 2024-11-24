#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 12:20
FileName: P3074. 重新分装苹果
Description:
"""
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        for i, cap in enumerate(capacity):
            if total <= cap:
                return i + 1
            total -= cap
        return -1


if __name__ == '__main__':
    solution = Solution().minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2])
    print(solution)
