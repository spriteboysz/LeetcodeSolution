#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 14:36
FileName: P1346. 检查整数及其两倍数是否存在.py
Description:
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        seen = set(arr)
        return any(num * 2 in seen for num in seen if num != 0)


if __name__ == '__main__':
    solution = Solution().checkIfExist(arr=[10, 2, 5, 3])
    print(solution)
