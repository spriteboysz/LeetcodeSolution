#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-19 12:22
FileName: P1952. 三除数.py
Description:
"""


class Solution:
    def isThree(self, n: int) -> bool:
        target = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return n in {num ** 2 for num in target}



if __name__ == '__main__':
    solution = Solution().isThree(4)
    print(solution)
