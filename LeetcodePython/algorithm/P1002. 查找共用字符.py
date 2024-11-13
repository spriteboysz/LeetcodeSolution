#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 21:20
FileName: P1002. 查找共用字符
Description:
"""
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabet = [101] * 26
        for word in words:
            for i in range(26):
                alphabet[i] = min(alphabet[i], word.count(chr(i + ord('a'))))
        common = [chr(i + ord('a')) * cnt for i, cnt in enumerate(alphabet) if cnt > 0]
        return list(''.join(common))


if __name__ == '__main__':
    solution = Solution().commonChars(words=["bella", "label", "roller"])
    print(solution)
