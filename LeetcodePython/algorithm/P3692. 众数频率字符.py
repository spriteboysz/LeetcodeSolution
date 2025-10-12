#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-10-12 12:08
FileName: P3692. 众数频率字符.py
Description:
"""

from collections import defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        frequency = defaultdict(list)
        for k, v in counter.items():
            frequency[v].append(k)
        frequency = {''.join(v): k for k, v in frequency.items()}
        return sorted(frequency.keys(), key=lambda el: (len(el), frequency.get(el)))[-1]


if __name__ == '__main__':
    s = Solution().majorityFrequencyGroup(s="aaabbbccdddde")
    print(s)
