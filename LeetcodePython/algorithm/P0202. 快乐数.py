#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:35
FileName: P0202. 快乐数
Description:
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([num * num for num in map(int, list(str(n)))])
            if n == 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().isHappy(19)
    print(solution)
