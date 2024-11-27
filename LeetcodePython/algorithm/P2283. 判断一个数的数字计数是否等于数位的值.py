#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 21:46
FileName: P2283. 判断一个数的数字计数是否等于数位的值
Description:
"""

from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        counter1 = {i: int(cnt) for i, cnt in enumerate(num)}
        counter2 = {int(k): v for k, v in Counter(num).items()}
        for k, v in counter1.items():
            if v != counter2.get(k, 0):
                return False
        for k, v in counter2.items():
            if v != counter1.get(k, 0):
                return False
        return True


if __name__ == '__main__':
    solution = Solution().digitCount('1210')
    print(solution)
