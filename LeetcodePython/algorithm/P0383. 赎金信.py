#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 21:08
FileName: P0383. 赎金信
Description:
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1, dic2 = Counter(ransomNote), Counter(magazine)
        for k, v in dic1.items():
            if v > dic2.get(k, 0):
                return False
        return True


if __name__ == '__main__':
    solution = Solution().canConstruct(ransomNote="aa", magazine="aab")
    print(solution)
