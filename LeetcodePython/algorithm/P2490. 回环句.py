#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-25 11:48
FileName: P2490. 回环句
Description:
"""

from icecream import ic


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i, _ in enumerate(words):
            if words[i][0] != words[i - 1][-1]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().isCircularSentence(sentence="leetcode exercises sound delightful")
    ic(solution)
