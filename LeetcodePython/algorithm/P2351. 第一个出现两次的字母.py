#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 22:48
FileName: P2351. 第一个出现两次的字母
Description:
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            else:
                return ch
        return 'Error'


if __name__ == '__main__':
    solution = Solution().repeatedCharacter(s="abccbaacz")
    print(solution)
