#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-11 22:26
FileName: algorithm/P2452. 距离字典两次编辑以内的单词.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        words = []
        for query in queries:
            for root in dictionary:
                if sum(ch1 != ch2 for ch1, ch2 in zip(query, root)) <= 2:
                    words.append(query)
                    break
        return words


if __name__ == '__main__':
    solution = Solution().twoEditWords(queries=["word", "note", "ants", "wood"], dictionary=["wood", "joke", "moat"])
    ic(solution)
