#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 20:53
FileName: P1684. 统计一致字符串的数目
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set(allowed)
        return sum(seen | set(word) == seen for word in words)


if __name__ == '__main__':
    solution = Solution().countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
    ic(solution)
