#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 22:26
FileName: P1078. Bigram 分词
Description:
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[i] for i in range(2, len(words)) if words[i - 2] == first and words[i - 1] == second]


if __name__ == '__main__':
    solution = Solution().findOcurrences(text="alice is a good girl she is a good student",
                                         first="a",
                                         second="good")
    print(solution)
