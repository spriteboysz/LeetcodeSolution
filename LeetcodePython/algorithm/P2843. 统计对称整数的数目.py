#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 22:25
FileName: P2843. 统计对称整数的数目
Description:
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for num in range(low, high + 1):
            ss = str(num)
            if len(ss) % 2 == 1:
                continue
            if sum(map(int, ss[:len(ss) // 2])) * 2 == sum(map(int, ss)):
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countSymmetricIntegers(1, 100)
    print(solution)
