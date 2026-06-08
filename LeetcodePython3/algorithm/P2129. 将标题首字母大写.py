#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-08 23:01
FileName: P2129. 将标题首字母大写.py
Description:
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(word.lower() if len(word) <= 2 else word.capitalize() for word in title.strip().split())


if __name__ == '__main__':
    solution = Solution().capitalizeTitle(title="First leTTeR of EACH Word")
    print(solution)
