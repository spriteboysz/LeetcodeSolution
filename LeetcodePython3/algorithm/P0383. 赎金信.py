#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 19:53
FileName: P0383. 赎金信.py
Description:
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1, count2 = Counter(ransomNote), Counter(magazine)
        for ch, cnt in count1.items():
            if count2.get(ch, 0) < cnt:
                return False
        return True


if __name__ == '__main__':
    solution = Solution().canConstruct(ransomNote="aa", magazine="aab")
    print(solution)
