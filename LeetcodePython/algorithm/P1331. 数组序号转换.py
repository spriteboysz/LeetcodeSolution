#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 09:31
FileName: P1331. 数组序号转换
Description:
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        data = {num: i for i, num in enumerate(sorted(set(arr)))}
        return [data[num] + 1 for i, num in enumerate(arr)]


if __name__ == '__main__':
    solution = Solution().arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12])
    print(solution)
