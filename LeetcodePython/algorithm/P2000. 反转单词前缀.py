#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-28 23:47
FileName: P2000. 反转单词前缀
Description:
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        return word[:index + 1][::-1] + word[index + 1:]


if __name__ == '__main__':
    solution = Solution().reversePrefix(word="abcdefd", ch="z")
    print(solution)
