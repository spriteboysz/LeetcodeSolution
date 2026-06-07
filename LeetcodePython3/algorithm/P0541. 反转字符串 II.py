#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:43
FileName: P0541. 反转字符串 II.py
Description:
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i:i + k][::-1] + s[i + k:i + 2 * k] for i in range(0, len(s), k * 2))


if __name__ == '__main__':
    solution = Solution().reverseStr(s="abcdefg", k=2)
    print(solution)
