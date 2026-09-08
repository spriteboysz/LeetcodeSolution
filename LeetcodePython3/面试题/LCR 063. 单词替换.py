#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 14:02
FileName: 面试题/LCR 063. 单词替换.py
Description: 
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = sentence.strip().split()
        seen = dict()
        for i, word in enumerate(words):
            if word in seen:
                if seen.get(word) != 'No Found':
                    words[i] = seen.get(word)
                continue
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    seen[word] = root
                    break
            else:
                seen[word] = 'No Found'
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().replaceWords(
        dictionary=["cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery"
    )
    print('<None>' if not solution else f'{solution=}')
