#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-12 22:48
FileName: P0151. 反转字符串中的单词
Description:
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


if __name__ == '__main__':
    solution = Solution().reverseWords(s="the sky is blue")
    print(solution)
