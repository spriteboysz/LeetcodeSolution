#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 09:45
FileName: algorithm/P0811. 子域名访问计数.py
Description: 
"""
from collections import defaultdict

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domains = cpdomain.split()
            domains = [d for d in domains.split('.')]
            for i in range(len(domains)):
                dic['.'.join(domains[i:])] += int(cnt)
        return [f'{v} {k}' for k, v in dic.items()]


if __name__ == '__main__':
    solution = Solution().subdomainVisits([
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org"
    ])
    print(solution)
