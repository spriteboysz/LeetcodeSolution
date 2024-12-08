#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:29
FileName: P0648. 单词替换
Description:
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        ss = []
        for word in sentence.split():
            for root in dictionary:
                if word.startswith(root):
                    ss.append(root)
                    break
            else:
                ss.append(word)
        return ' '.join(ss)


if __name__ == '__main__':
    solution = Solution().replaceWords(dictionary=["cat", "bat", "rat"],
                                       sentence="the cattle was rattled by the battery")
    print(solution)
