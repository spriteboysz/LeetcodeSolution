#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 12:02
FileName: P0482. 密钥格式化
Description:
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ss = [ch.upper() for ch in s if ch.isalnum()][::-1]
        return '-'.join([''.join(ss[i:i + k]) for i in range(0, len(ss), k)])[::-1]


if __name__ == '__main__':
    solution = Solution().licenseKeyFormatting(s="2-5g-3-J", k=2)
    print(solution)
