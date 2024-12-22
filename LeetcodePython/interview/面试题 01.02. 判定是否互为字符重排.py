#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 20:13
FileName: 面试题 01.02. 判定是否互为字符重排
Description:
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(list(s1)) == sorted(list(s2))


if __name__ == '__main__':
    solution = Solution().CheckPermutation(s1="abc", s2="bca")
    print(solution)
