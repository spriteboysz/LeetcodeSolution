#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-19 22:48
FileName: P0791. 自定义字符串排序
Description:
"""

from icecream import ic


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {ch: i for i, ch in enumerate(order)}
        return ''.join(sorted(s, key=lambda el: dic.get(el, 27)))


if __name__ == '__main__':
    solution = Solution().customSortString(order="cba", s="abcd")
    ic(solution)
