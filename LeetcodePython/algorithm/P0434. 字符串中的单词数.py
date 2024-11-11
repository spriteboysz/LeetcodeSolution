#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:20
FileName: P0434. 字符串中的单词数
Description:
"""


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split())


if __name__ == '__main__':
    solution = Solution().countSegments("Hello, my name is John")
    print(solution)
