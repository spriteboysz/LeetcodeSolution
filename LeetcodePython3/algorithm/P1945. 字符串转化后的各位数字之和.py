#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:42
FileName: P1945. 字符串转化后的各位数字之和.py
Description:
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        for _ in range(k):
            ss = str(sum(int(ch) for ch in ss))
        return int(ss)


if __name__ == '__main__':
    solution = Solution().getLucky(s="leetcode", k=2)
    print(solution)
