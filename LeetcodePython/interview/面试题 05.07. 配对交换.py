#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 22:46
FileName: 面试题 05.07. 配对交换
Description:
"""


class Solution:
    def exchangeBits(self, num: int) -> int:
        ss = list(bin(num)[2:].rjust(64, '0'))
        ss[::2], ss[1::2] = ss[1::2], ss[::2]
        return int(''.join(ss), 2)


if __name__ == '__main__':
    solution = Solution().exchangeBits(3)
    print(solution)
