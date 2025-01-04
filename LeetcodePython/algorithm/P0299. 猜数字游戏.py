#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 11:13
FileName: P0299. 猜数字游戏
Description:
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic1, dic2 = defaultdict(int), defaultdict(int)
        count1, count2 = 0, 0
        for ch1, ch2 in zip(secret, guess):
            if ch1 == ch2:
                count1 += 1
            else:
                dic1[ch1] += 1
                dic2[ch2] += 1
        for k, v in dic1.items():
            count2 += min(v, dic2[k])
        return f'{count1}A{count2}B'


if __name__ == '__main__':
    solution = Solution().getHint(secret="1807", guess="7810")
    print(solution)
