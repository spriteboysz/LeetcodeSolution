#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 19:51
FileName: P0693. 交替位二进制数
Description:
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s, ss = bin(n)[2:], []
        for i, ch in enumerate(s):
            if i % 2 == 0:
                ss.append(str(1 - int(ch)))
            else:
                ss.append(ch)
        return len(set(ss)) == 1


if __name__ == '__main__':
    solution = Solution().hasAlternatingBits(5)
    print(solution)
