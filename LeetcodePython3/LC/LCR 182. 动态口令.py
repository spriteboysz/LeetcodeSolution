#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 22:56
FileName: LCR/LCR 182. 动态口令.py
Description: 
"""


class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:] + password[:target]


if __name__ == '__main__':
    solution = Solution().dynamicPassword(password="s3cur1tyC0d3", target=4)
    print(solution)
