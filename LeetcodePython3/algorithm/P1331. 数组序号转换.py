#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:26
FileName: P1331. 数组序号转换.py
Description:
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [dic.get(num, 0) for num in arr]


if __name__ == '__main__':
    solution = Solution().arrayRankTransform(arr=[40, 40, 10, 20, 30])
    print(solution)
