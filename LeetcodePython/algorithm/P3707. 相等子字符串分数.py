#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 11:47
FileName: P3707. 相等子字符串分数.py
Description:
"""


class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = [ord(ch) - ord('a') + 1 for ch in s]
        total = sum(scores)
        if total % 2 == 1:
            return False
        acc = 0
        for score in scores:
            acc += score
            if acc == total // 2:
                return True
        return False


if __name__ == '__main__':
    s = Solution().scoreBalance('adcb')
    print(s)
