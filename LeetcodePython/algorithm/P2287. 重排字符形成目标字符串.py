#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:12
FileName: P2287. 重排字符形成目标字符串
Description:
"""
from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter1 = Counter(target)
        counter2 = Counter(s)
        return min([counter2.get(k, 0) // v for k, v in counter1.items()])


if __name__ == '__main__':
    solution = Solution().rearrangeCharacters(s="ilovecodingonleetcode", target="code")
    print(solution)
