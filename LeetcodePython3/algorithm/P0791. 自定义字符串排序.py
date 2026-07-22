#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-21 22:57
FileName: P0791. 自定义字符串排序.py
Description:
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {ch: i for i, ch in enumerate(order)}
        return ''.join(sorted(list(s), key=lambda ch: dic.get(ch, 27)))


if __name__ == '__main__':
    solution = Solution().customSortString(order="cba", s="abcd")
    print(solution)
