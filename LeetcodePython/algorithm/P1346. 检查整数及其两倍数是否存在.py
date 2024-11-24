#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 11:35
FileName: P1346. 检查整数及其两倍数是否存在
Description:
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        seen = set(arr) - {0}
        for num in seen:
            if num * 2 in seen:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().checkIfExist(arr=[10, 2, 5, 3])
    print(solution)
