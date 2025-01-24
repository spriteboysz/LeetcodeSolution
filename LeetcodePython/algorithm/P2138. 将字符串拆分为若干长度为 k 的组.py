#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-24 22:11
FileName: P2138. 将字符串拆分为若干长度为 k 的组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            mod = k - len(s) % k
            s += fill * mod
        return [s[i:i + k] for i in range(0, len(s), k)]


if __name__ == '__main__':
    solution = Solution().divideString(s="abcdefghij", k=3, fill="x")
    ic(solution)
