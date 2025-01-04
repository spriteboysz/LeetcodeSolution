#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 20:49
FileName: P1790. 仅执行一次字符串交换能否使两个字符串相等
Description:
"""

from icecream import ic


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        ss1, ss2 = [], []
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                ss1.append(ch1)
                ss2.append(ch2)
        return len(ss1) == len(ss2) == 2 and sorted(ss1) == sorted(ss2)


if __name__ == '__main__':
    solution = Solution().areAlmostEqual(s1="bank", s2="kanb")
    ic(solution)
