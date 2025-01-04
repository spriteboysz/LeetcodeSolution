#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:13
FileName: P1897. 重新分配字符使所有字符串都相等
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter(''.join(words))
        return all(cnt % len(words) == 0 for cnt in counter.values())


if __name__ == '__main__':
    solution = Solution().makeEqual(words=["abc", "aabc", "bc"])
    ic(solution)
