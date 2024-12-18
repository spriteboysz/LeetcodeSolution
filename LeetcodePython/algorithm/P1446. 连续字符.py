#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-17 23:15
FileName: P1446. 连续字符
Description:
"""


class Solution:
    def maxPower(self, s: str) -> int:
        maximum, curr = 1, 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr += 1
                maximum = max(maximum, curr)
            else:
                curr = 1
        return maximum


if __name__ == '__main__':
    solution = Solution().maxPower(s="abbcccddddeeeeedcba")
    print(solution)
