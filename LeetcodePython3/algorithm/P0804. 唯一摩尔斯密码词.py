#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:23
FileName: P0804. 唯一摩尔斯密码词.py
Description:
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                      '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        return len({''.join(morse_code[ord(ch) - ord('a')] for ch in word) for word in words})


if __name__ == '__main__':
    solution = Solution().uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
    print(solution)
