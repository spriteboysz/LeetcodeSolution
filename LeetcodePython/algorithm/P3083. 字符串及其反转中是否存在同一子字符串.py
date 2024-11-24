#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:56
FileName: P3083. 字符串及其反转中是否存在同一子字符串
Description:
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i + 2][::-1] in s:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().isSubstringPresent(s="leetcode")
    print(solution)
