#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 23:26
FileName: P1816. 截断句子
Description:
"""

from icecream import ic


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


if __name__ == '__main__':
    solution = Solution().truncateSentence(s="Hello how are you Contestant", k=4)
    ic(solution)
