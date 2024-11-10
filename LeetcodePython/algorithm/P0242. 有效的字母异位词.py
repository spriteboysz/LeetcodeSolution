#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:01
FileName: P0242. 有效的字母异位词
Description:
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution().isAnagram('rat', 'tar')
    print(solution)
