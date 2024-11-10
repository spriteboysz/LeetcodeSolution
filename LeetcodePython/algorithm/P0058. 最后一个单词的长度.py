#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:11
FileName: P0058. 最后一个单词的长度
Description:
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


if __name__ == '__main__':
    solution = Solution().lengthOfLastWord(s="   fly me   to   the moon  ")
    print(solution)
