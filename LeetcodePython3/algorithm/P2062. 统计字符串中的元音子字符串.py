#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-12 22:09
FileName: P2062. 统计字符串中的元音子字符串.py
Description:
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        for i in range(len(word)):
            for j in range(i + 4, len(word)):
                if set(word[i:j + 1]) == {'a', 'e', 'i', 'o', 'u'}:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countVowelSubstrings(word="cuaieuouac")
    print(solution)
