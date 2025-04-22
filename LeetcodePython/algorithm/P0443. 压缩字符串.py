#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 21:14
FileName: algorithm/P0443. 压缩字符串.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt, cur, pos = 1, 1, 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cur += 1
            else:
                if cur != 1:
                    n = len(str(cur))
                    chars[pos:pos + n] = list(str(cur))
                    pos += n
                chars[pos] = chars[i]
                pos += 1
                cur = 1
        if cur != 1:
            n = len(str(cur))
            chars[pos:pos + n] = list(str(cur))
            pos += n
        chars = chars[:pos]
        ic(chars)
        return pos


if __name__ == '__main__':
    solution = Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    ic(solution)
