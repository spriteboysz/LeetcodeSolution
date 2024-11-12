#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-12 23:23
FileName: P0804. 唯一摩尔斯密码词
Description:
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
               '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        seen = set()
        for word in words:
            moss = ''.join([mos[ord(ch) - ord('a')] for ch in word])
            seen.add(moss)
            print(moss)
        return len(seen)


if __name__ == '__main__':
    solution = Solution().uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
    print(solution)
