#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:13
FileName: P0744. 寻找比目标字母大的最小字母.py
Description:
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(target) < ord(letter):
                return letter
        return letters[0]


if __name__ == '__main__':
    solution = Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='a')
    print(solution)
