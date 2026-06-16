#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 23:13
FileName: P2138. 将字符串拆分为若干长度为 k 的组.py
Description:
"""
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        return [s[i:i + k] for i in range(0, len(s), k)]


if __name__ == '__main__':
    solution = Solution().divideString(s="abcdefghij", k=3, fill='x')
    print(solution)
