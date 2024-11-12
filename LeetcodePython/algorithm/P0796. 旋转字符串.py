#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:22
FileName: P0796. 旋转字符串
Description:
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s


if __name__ == '__main__':
    solution = Solution().rotateString(s="abcde", goal="cdeab")
    print(solution)
