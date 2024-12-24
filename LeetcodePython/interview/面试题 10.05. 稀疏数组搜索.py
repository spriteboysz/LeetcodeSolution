#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 22:58
FileName: 面试题 10.05. 稀疏数组搜索
Description:
"""
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i, word in enumerate(words):
            if word == s:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ball")
    print(solution)
