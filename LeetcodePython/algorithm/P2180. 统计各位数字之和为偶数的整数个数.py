#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:48
FileName: P2180. 统计各位数字之和为偶数的整数个数
Description:
"""


class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(2, num + 1):
            if sum(map(int, list(str(i)))) % 2 == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countEven(30)
    print(solution)
