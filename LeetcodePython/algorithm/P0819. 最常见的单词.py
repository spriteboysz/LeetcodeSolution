#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 23:24
FileName: P0819. 最常见的单词
Description:
"""
from typing import List
from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'[^a-zA-Z]+', paragraph.lower())
        count = defaultdict(int)
        for word in words:
            if word not in set(banned) and word != '':
                count[word] += 1
        maximum = max(count.values())
        for word, cnt in count.items():
            if cnt == maximum:
                return word
        return ''


if __name__ == '__main__':
    solution = Solution().mostCommonWord(paragraph="..Bob hit a ball, the hit BALL flew far after it was hit.",
                                         banned=["hit"])
    print(solution)
