#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 23:01
FileName: P1394. 找出数组中的幸运数
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        lucky = [num for num, cnt in counter.items() if cnt == num]
        return max(lucky) if lucky else -1


if __name__ == '__main__':
    solution = Solution().findLucky(arr=[1, 2, 2, 3, 3, 3])
    print(solution)
