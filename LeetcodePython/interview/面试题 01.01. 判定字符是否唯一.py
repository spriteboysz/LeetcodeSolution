#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 20:10
FileName: 面试题 01.01. 判定字符是否唯一
Description:
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


if __name__ == '__main__':
    solution = Solution().isUnique("leetcode")
    print(solution)
