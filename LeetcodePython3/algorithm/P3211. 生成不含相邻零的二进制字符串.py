#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 09:14
FileName: P3211. 生成不含相邻零的二进制字符串.py
Description:
"""
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        paths, path = [], [''] * n

        def backtrace(i):
            if i == n:
                paths.append(''.join(path))
                return
            path[i] = '1'
            backtrace(i + 1)

            if i == 0 or path[i - 1] == '1':
                path[i] = '0'
                backtrace(i + 1)

        backtrace(0)
        return paths


if __name__ == '__main__':
    solution = Solution().validStrings(4)
    print(solution)
