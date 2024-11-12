#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:17
FileName: P0521. 最长特殊序列 Ⅰ
Description:
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == '__main__':
    solution = Solution().findLUSlength(a="aba", b="cdc")
    print(solution)
