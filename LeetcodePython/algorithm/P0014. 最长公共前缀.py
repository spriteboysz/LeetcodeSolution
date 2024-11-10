#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 16:39
FileName: P0014. 最长公共前缀
Description:
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        for pref in zip(*strs):
            if len(set(pref)) == 1:
                k += 1
            else:
                break
        return strs[0][:k]


if __name__ == '__main__':
    solution = Solution().longestCommonPrefix(strs=["flower", "flow", "flight"])
    print(solution)
    solution = Solution().longestCommonPrefix(strs = ["dog","racecar","car"])
    print(solution)
