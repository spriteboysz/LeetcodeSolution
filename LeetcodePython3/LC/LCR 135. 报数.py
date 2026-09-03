#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:28
FileName: LC/LCR 135. 报数.py
Description: 
"""
from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        return [num for num in range(1, 10 ** cnt)]


if __name__ == '__main__':
    solution = Solution().countNumbers(2)
    print(solution)
