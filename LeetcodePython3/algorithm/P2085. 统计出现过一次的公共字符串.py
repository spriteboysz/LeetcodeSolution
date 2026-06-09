#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 22:55
FileName: P2085. 统计出现过一次的公共字符串.py
Description:
"""
from collections import Counter

from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1, counter2 = Counter(words1), Counter(words2)
        return sum(cnt == 1 and counter2.get(word, 0) == 1 for word, cnt in counter1.items())


if __name__ == '__main__':
    solution = Solution().countWords(
        words1=["leetcode", "is", "amazing", "as", "is"],
        words2=["amazing", "leetcode", "is"]
    )
    print(solution)
