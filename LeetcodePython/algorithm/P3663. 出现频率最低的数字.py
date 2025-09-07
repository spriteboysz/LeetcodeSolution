#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-07 22:26
FileName: P3663. 出现频率最低的数字.py
Description:
"""

from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counter = Counter(str(n))
        minimum = min(counter.values())
        for k in range(10):
            if counter[str(k)] == minimum:
                return k
        return -1


if __name__ == '__main__':
    s = Solution().getLeastFrequentDigit(n=1553322)
    print(s)
