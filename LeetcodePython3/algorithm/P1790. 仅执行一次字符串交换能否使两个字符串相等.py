#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 23:09
FileName: P1790. 仅执行一次字符串交换能否使两个字符串相等.py
Description:
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = []
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                diff.append([ch1, ch2])
        return len(diff) == 2 and diff[0] == diff[-1][::-1]


if __name__ == '__main__':
    solution = Solution().areAlmostEqual(s1="bank", s2="kanb")
    print(solution)
