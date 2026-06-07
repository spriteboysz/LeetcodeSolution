#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:21
FileName: P0796. 旋转字符串.py
Description:
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) == len(s) and goal in s + s


if __name__ == '__main__':
    solution = Solution().rotateString(s="abcde", goal="cdeab")
    print(solution)
