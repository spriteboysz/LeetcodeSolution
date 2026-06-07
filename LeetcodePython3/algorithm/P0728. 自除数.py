#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 10:07
FileName: P0728. 自除数.py
Description:
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if all(ch != '0' and num % int(ch) == 0 for ch in str(num))]


if __name__ == '__main__':
    solution = Solution().selfDividingNumbers(1, 22)
    print(solution)
