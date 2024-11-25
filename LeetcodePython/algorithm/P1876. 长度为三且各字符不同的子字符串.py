#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:51
FileName: P1876. 长度为三且各字符不同的子字符串
Description:
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        subs = [s[i:i + 3] for i in range(0, len(s) - 2)]
        return sum([len(set(list(sub))) == len(sub) for sub in subs])


if __name__ == '__main__':
    solution = Solution().countGoodSubstrings(s="aababcabc")
    print(solution)
