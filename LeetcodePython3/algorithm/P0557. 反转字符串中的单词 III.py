#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 22:13
FileName: P0557. 反转字符串中的单词 III.py
Description:
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.strip().split())


if __name__ == '__main__':
    solution = Solution().reverseWords(s="Let's take LeetCode contest")
    print(solution)
