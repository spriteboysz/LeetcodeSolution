#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 22:58
FileName: P0386. 字典序排数.py
Description:
"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)


if __name__ == '__main__':
    solution = Solution().lexicalOrder(13)
    print(solution)
