#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:35
FileName: P2169. 得到 0 的操作数
Description:
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 * num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countOperations(num1=2, num2=3)
    print(solution)
