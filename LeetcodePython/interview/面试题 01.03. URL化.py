#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 10:29
FileName: 面试题 01.03. URL化
Description:
"""

from icecream import ic


class Solution:
    def replaceSpaces(self, s: str, length: int) -> str:
        return s[:length].replace(' ', '%20')


if __name__ == '__main__':
    solution = Solution().replaceSpaces("Mr John Smith    ", 13)
    ic(solution)
