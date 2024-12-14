#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 10:14
FileName: LCR 181. 字符串中的单词反转
Description:
"""

class Solution:
    def reverseMessage(self, message: str) -> str:
        return ' '.join(message.strip().split()[::-1])

if __name__ == '__main__':
    solution = Solution().reverseMessage(message = "  hello world!  ")
    print(solution)