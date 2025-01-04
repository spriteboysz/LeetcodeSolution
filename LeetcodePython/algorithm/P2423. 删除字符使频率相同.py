#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 22:49
FileName: P2423. 删除字符使频率相同
Description:
"""

from collections import Counter

from icecream import ic


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = sorted(Counter(word).values())
        if len(counter) == 1:
            return True
        if counter[0] == 1 and len(set(counter[1:])) == 1:
            return True
        return counter[-1] == counter[-2] + 1 and len(set(counter[:-1])) == 1


if __name__ == '__main__':
    solution = Solution().equalFrequency('aaccc')
    ic(solution)
