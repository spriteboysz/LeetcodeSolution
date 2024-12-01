#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 16:18
FileName: P2937. 使三个字符串相等
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
        if cnt < 1:
            return -1
        return len(s1) + len(s2) + len(s3) - cnt * 3


if __name__ == '__main__':
    solution = Solution().findMinimumOperations(s1="abc", s2="abb", s3="ab")
    print(solution)
