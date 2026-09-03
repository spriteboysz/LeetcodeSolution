#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 20:35
FileName: LC/LCR 181. 字符串中的单词反转.py
Description: 
"""


class Solution:
    def reverseMessage(self, message: str) -> str:
        words = message.strip().split()
        return ' '.join(words[::-1])


if __name__ == '__main__':
    solution = Solution().reverseMessage(message="  hello world!  ")
    print(solution)
