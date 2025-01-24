#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 22:06
FileName: P2129. 将标题首字母大写
Description:
"""

from icecream import ic


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = [word.capitalize() for word in title.split()]
        for i, word in enumerate(words):
            if len(word) <= 2:
                words[i] = word.lower()
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().capitalizeTitle("capiTalIze tHe titLe")
    ic(solution)
