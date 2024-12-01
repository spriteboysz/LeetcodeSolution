#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 20:14
FileName: P0744. 寻找比目标字母大的最小字母
Description:
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = set(letters)
        letters = [letter for letter in letters if letter in seen]
        for letter in letters:
            if ord(target) < ord(letter):
                return letter
        return letters[0]


if __name__ == '__main__':
    solution = Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a")
    print(solution)
