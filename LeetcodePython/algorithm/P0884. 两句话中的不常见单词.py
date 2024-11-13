#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 21:11
FileName: P0884. 两句话中的不常见单词
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = s1.split(), s2.split()
        counter1, counter2 = Counter(words1), Counter(words2)
        return [word for word in [*words1, *words2] if counter1.get(word, 0) + counter2.get(word, 0) == 1]


if __name__ == '__main__':
    solution = Solution().uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour")
    print(solution)
