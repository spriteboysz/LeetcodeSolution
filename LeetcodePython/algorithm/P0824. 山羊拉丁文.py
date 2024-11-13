#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 20:36
FileName: P0824. 山羊拉丁文
Description:
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word[0] not in vowel:
                word = word[1:] + word[0]
            words[i] = word + 'ma' + 'a' * (i + 1)
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().toGoatLatin(sentence="I speak Goat Latin")
    print(solution)
