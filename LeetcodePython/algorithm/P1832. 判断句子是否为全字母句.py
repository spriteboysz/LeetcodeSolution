#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 22:37
FileName: P1832. 判断句子是否为全字母句
Description:
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(list(sentence))) == 26

if __name__ == '__main__':
    solution = Solution().checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog")
    print(solution)