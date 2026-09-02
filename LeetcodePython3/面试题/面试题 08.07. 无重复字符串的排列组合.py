#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 09:19
FileName: 面试题/面试题 08.07. 无重复字符串的排列组合.py
Description: 
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        paths = []

        def backtrack(path, res):
            if len(res) == 0:
                paths.append(''.join(path))
                return
            for i, c in enumerate(res):
                path.append(c)
                backtrack(path, res[:i] + res[i + 1:])
                path.pop()

        backtrack([], list(s))
        return paths


if __name__ == '__main__':
    solution = Solution().permutation('qwe')
    print(solution)
