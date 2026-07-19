#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 17:07
FileName: P0648. 单词替换.py
Description:
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary, key=len)
        dic = {}
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word in dic:
                words[i] = dic.get(word, '')
            else:
                for root in dictionary:
                    if word.startswith(root):
                        words[i] = root
                        dic[word] = root
                        break
                else:
                    words[i] = word
                    dic[word] = word
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().replaceWords(
        dictionary=["cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery"
    )
    print(solution)
