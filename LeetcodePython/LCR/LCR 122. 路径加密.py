#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 10:22
FileName: LCR 122. 路径加密
Description:
"""


class Solution:
    def pathEncryption(self, path: str) -> str:
        return path.replace('.', ' ')


if __name__ == '__main__':
    solution = Solution().pathEncryption(path="a.aef.qerf.bb")
    print(solution)
