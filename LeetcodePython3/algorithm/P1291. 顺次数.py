#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 17:01
FileName: algorithm/P1291. 顺次数.py
Description: 
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        def generate(n):
            arr = []
            for a in range(1, 10 - n + 1):
                ss = 0
                for b in range(n):
                    ss = 10 * ss + a + b
                arr.append(ss)
            return arr

        nums = []
        n1, n2 = len(str(low)), len(str(high))
        for i in range(n1, n2 + 1):
            nums.extend(generate(i))
        return [num for num in nums if low <= num <= high]


if __name__ == '__main__':
    solution = Solution().sequentialDigits(1000, 13000)
    print('<None>' if solution is None else f'{solution=}')
