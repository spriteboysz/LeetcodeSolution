#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 22:53
FileName: P1566. 重复至少 K 次且长度为 M 的模式.py
Description:
"""
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        ss = '#'.join(map(str, arr))
        for i in range(len(arr)):
            if i + m >= len(arr):
                break
            match = '#'.join(map(str, arr[i:i + m] * k))
            if match in ss:
                print(match, ss)
                return True
        return False


if __name__ == '__main__':
    solution = Solution().containsPattern(arr=[2, 2, 2, 2], m=2, k=3)
    print(solution)
