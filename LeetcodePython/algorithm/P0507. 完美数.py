#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 22:15
FileName: P0507. 完美数
Description:
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        seen = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                if i in seen:
                    break
                else:
                    seen.add(i)
                    seen.add(num // i)
        return sum(seen) == num * 2


if __name__ == '__main__':
    solution = Solution().checkPerfectNumber(28)
    print(solution)
