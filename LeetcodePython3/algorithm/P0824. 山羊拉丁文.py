#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-13 12:44
FileName: P0824. 山羊拉丁文.py
Description:
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word[0].lower() in 'aeiou':
                words[i] = word + 'ma'
            else:
                words[i] = word[1:] + word[0] + 'ma'
        return ' '.join(word + 'a' * (i + 1) for i, word in enumerate(words))


if __name__ == '__main__':
    solution = Solution().toGoatLatin(sentence="I speak Goat Latin")
    print(solution)
