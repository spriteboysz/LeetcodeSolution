#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-23 17:54
FileName: P1338. 数组大小减半
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for num in arr:
            dic[num] += 1
        count = sorted(dic.values(), reverse=True)
        acc = 0
        for i, cnt in enumerate(count):
            acc += cnt
            if acc >= len(arr) // 2:
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    ic(solution)
