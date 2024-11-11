#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:12
FileName: P0709. 转换成小写字母
Description:
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == '__main__':
    solution = Solution().toLowerCase(s="Hello")
    print(solution)
