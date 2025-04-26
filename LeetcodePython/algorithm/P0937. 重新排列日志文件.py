#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 10:27
FileName: algorithm/P0937. 重新排列日志文件.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comp(log: str) -> tuple:
            a, b = log.split(' ', maxsplit=1)
            if b[0].isalpha():
                return 0, b, a
            return (1,)

        return sorted(logs, key=comp)


if __name__ == '__main__':
    solution = Solution().reorderLogFiles(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    ic(solution)
