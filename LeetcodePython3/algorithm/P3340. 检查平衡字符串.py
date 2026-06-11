#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 22:48
FileName: P3340. 检查平衡字符串.py
Description:
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(ch) for i, ch in enumerate(num) if i % 2 == 0) * 2 == sum(map(int, list(num)))


if __name__ == '__main__':
    solution = Solution().isBalanced('24123')
    print(solution)
