#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 22:58
FileName: P1576. 替换所有的问号.py
Description:
"""
import random
from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        ss = list(s)
        for i, ch in enumerate(ss):
            if ch != '?':
                continue
            seen = set()
            try:
                seen.add(ss[i - 1])
                seen.add(ss[i + 1])
            except IndexError:
                pass
            for _ in range(100):
                target = random.choice(ascii_lowercase)
                if target not in seen:
                    ss[i] = target
                    break
            else:
                raise ValueError('Error')
        return ''.join(ss)


if __name__ == '__main__':
    solution = Solution().modifyString(s="????")
    print(solution)
