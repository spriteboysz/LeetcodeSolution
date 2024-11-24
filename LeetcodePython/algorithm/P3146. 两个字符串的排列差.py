#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:45
FileName: P3146. 两个字符串的排列差
Description:
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic1 = {ch: i for i, ch in enumerate(s)}
        dic2 = {ch: i for i, ch in enumerate(t)}
        return sum([abs(dic1[ch] - dic2[ch]) for ch in s])


if __name__ == '__main__':
    solution = Solution().findPermutationDifference(s="abc", t="bac")
    print(solution)
