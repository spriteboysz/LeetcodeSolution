#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 13:17
FileName: P1598. 文件夹操作日志搜集器.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(log)
        return len(stack)


if __name__ == '__main__':
    solution = Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"])
    print(solution)
