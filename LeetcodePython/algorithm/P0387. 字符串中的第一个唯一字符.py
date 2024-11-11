#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:02
FileName: P0387. 字符串中的第一个唯一字符
Description:
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i, ch in enumerate(s):
            if dic.get(ch, 0) == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution().firstUniqChar(s="loveleetcode")
    print(solution)
