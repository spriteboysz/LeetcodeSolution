#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-20 22:22
FileName: P3014. 输入单词需要的最少按键次数 I
Description:
"""
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = list(Counter(word).values())
        counter.sort(reverse=True)
        cnt = 0
        for i, el in enumerate(counter):
            if i < 8:
                cnt += el * 1
            elif i < 16:
                cnt += el * 2
            elif i < 24:
                cnt += el * 3
            else:
                cnt += el * 4
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumPushes('xycdefghijj')
    print(solution)
