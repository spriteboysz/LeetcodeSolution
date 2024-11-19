#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 23:09
FileName: P1342. 将数字变成 0 的操作次数
Description:
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numberOfSteps(14)
    print(solution)
