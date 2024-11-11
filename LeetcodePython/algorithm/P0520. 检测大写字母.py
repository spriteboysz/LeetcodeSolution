#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:47
FileName: P0520. 检测大写字母
Description:
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.upper(), word.lower(), word.capitalize()]


if __name__ == '__main__':
    solution = Solution().detectCapitalUse(word="USA")
    print(solution)
