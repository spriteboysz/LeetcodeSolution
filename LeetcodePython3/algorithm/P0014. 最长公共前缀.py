#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 13:19
FileName: P0014. 最长公共前缀.py
Description:
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(map(len, strs))
        for i in range(minimum):
            if len(set(word[i] for word in strs)) != 1:
                return strs[0][:i]
        return strs[0][:minimum]


if __name__ == '__main__':
    solution = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(solution)
