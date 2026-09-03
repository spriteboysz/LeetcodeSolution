#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 10:19
FileName: LC/LCR 122. 路径加密.py
Description: 
"""


class Solution:
    def pathEncryption(self, path: str) -> str:
        return path.replace('.', ' ')


if __name__ == '__main__':
    solution = Solution().pathEncryption("a.aef.qerf.bb")
    print(solution)
