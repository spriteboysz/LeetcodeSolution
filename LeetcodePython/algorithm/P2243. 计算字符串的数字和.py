#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 22:55
FileName: P2243. 计算字符串的数字和
Description:
"""

from icecream import ic


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ss = []
            for i in range(0, len(s), k):
                ss.append(str(sum(map(int, s[i:i + k]))))
            s = ''.join(ss)
        return s


if __name__ == '__main__':
    solution = Solution().digitSum(s="11111222223", k=3)
    ic(solution)
