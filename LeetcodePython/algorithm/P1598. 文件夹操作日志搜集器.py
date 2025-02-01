#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-31 23:02
FileName: P1598. 文件夹操作日志搜集器
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        high = 0
        for log in logs:
            if log == '../':
                if high:
                    high -= 1
            elif log == './':
                ...
            else:
                high += 1
        return high


if __name__ == '__main__':
    solution = Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"])
    ic(solution)
