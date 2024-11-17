#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 08:45
FileName: P0405. 数字转换为十六进制数
Description:
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ss = []
        if num < 0:
            num = num + 4294967296
        while num >= 16:
            num, mod = divmod(num, 16)
            ss.append(chars[mod])
        ss.append(chars[num])
        return ''.join(ss)[::-1]


if __name__ == '__main__':
    solution = Solution().toHex(26)
    print(solution)
