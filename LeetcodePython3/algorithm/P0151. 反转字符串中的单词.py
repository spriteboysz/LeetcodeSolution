#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 20:26
FileName: P0151. 反转字符串中的单词.py
Description:
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    solution = Solution().reverseWords("the sky is blue")
    print(solution)
