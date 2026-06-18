#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-17 22:49
FileName: P2937. 使三个字符串相等.py
Description:
"""


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        cnt = 0
        for ch1, ch2, ch3 in zip(s1, s2, s3):
            if ch1 == ch2 == ch3:
                cnt += 1
            else:
                break
        if cnt == 0:
            return -1
        return sum(len(el) - cnt for el in [s1, s2, s3])


if __name__ == '__main__':
    solution = Solution().findMinimumOperations(s1="a", s2="a", s3="a")
    print(solution)
