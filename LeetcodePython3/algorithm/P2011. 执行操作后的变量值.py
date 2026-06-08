#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 22:44
FileName: P2011. 执行操作后的变量值.py
Description:
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1] == '+' else -1 for op in operations)


if __name__ == '__main__':
    solution = Solution().finalValueAfterOperations(operations=["--X", "X++", "X++"])
    print(solution)
