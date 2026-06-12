#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-11 23:31
FileName: P3707. 相等子字符串分数.py
Description:
"""


class Solution:
    def scoreBalance(self, s: str) -> bool:
        nums = [ord(ch) - ord('a') + 1 for ch in s]
        total, acc = sum(nums), 0
        for num in nums:
            acc += num
            if acc * 2 == total:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().scoreBalance("abdcd")
    print(solution)
