#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 23:12
FileName: P3582. 为视频标题生成标签.py
Description:
"""


class Solution:
    def generateTag(self, caption: str) -> str:
        return '#' + ''.join(
            word.capitalize() if i != 0 else word.lower() for i, word in enumerate(caption.strip().split()))[:99]


if __name__ == '__main__':
    solution = Solution().generateTag(caption=" ")
    print(solution)
