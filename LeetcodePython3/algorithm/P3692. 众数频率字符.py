#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-04 13:01
FileName: P3692. 众数频率字符.py
Description:
"""
from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        dic = defaultdict(list)
        counter = Counter(s)
        for ch, cnt in counter.items():
            dic[cnt].append(ch)
        dic2 = {''.join(v): cnt for cnt, v in dic.items()}
        return sorted(dic2, key=lambda el: (len(el), dic2.get(el, 0)), reverse=True)[0]


if __name__ == '__main__':
    solution = Solution().majorityFrequencyGroup(s="pfpfgi")
    print(solution)
