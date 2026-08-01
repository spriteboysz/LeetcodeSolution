#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-01 15:25
FileName: P3992. 重新排列字符串以避免字符对.py
Description:
"""
from typing import Counter


class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        counter = Counter(s)
        ss = [y * counter.get(y, 0), x * counter.get(x, 0)]
        for ch, num in counter.items():
            if ch == x or ch == y:
                continue
            ss.append(ch * num)
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().rearrangeString(s="aabc", x="a", y="c")
    print(solution)
