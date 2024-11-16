#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 12:10
FileName: P0541. 反转字符串 II
Description:
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = ''
        for i in range(0, len(s), k * 2):
            sub = s[i:i + k * 2]
            ss += sub[:k][::-1] + sub[k:]
        return ss


if __name__ == '__main__':
    solution = Solution().reverseStr(s="abcde", k=2)
    print(solution)
