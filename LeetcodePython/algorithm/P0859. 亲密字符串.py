#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 20:43
FileName: P0859. 亲密字符串
Description:
"""
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return max(Counter(s).values()) >= 2
        char1, char2 = [], []
        for ch1, ch2 in zip(s, goal):
            if ch1 != ch2:
                char1.append(ch1)
                char2.append(ch2)
        return len(char1) == 2 and char1 == char2[::-1]


if __name__ == '__main__':
    solution = Solution().buddyStrings(s="aa", goal="aa")
    print(solution)
