#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 22:17
FileName: P0482. 密钥格式化.py
Description:
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ss = [ch.upper() for ch in s if ch.isalnum()][::-1]
        for i, ch in enumerate(ss):
            if i and i % k == 0:
                ss[i] = f'{ch}-'
        return ''.join(ss[::-1])


if __name__ == '__main__':
    solution = Solution().licenseKeyFormatting(s="5F3Z-2e-9-w", k=4)
    print(solution)
