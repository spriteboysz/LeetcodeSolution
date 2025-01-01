#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 18:55
FileName: LCR 063. 单词替换
Description:
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = sentence.strip().split()
        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().replaceWords(dictionary=["cat", "bat", "rat"],
                                       sentence="the cattle was rattled by the battery")
    print(solution)
