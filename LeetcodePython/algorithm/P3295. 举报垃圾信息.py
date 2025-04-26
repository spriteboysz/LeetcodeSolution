#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 16:23
FileName: algorithm/P3295. 举报垃圾信息.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_words = set(bannedWords)
        cnt = 0
        for word in message:
            if word in banned_words:
                cnt += 1
            if cnt >= 2:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().reportSpam(message=["hello", "world", "leetcode"], bannedWords=["world", "hello"])
    ic(solution)
