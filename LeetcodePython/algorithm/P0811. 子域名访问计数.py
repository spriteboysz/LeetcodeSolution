#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-17 23:31
FileName: P0811. 子域名访问计数
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        data = defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split()
            ss = domain.split('.')
            for i in range(len(ss)):
                data['.'.join(ss[i:])] += int(cnt)
        return [f'{v} {k}' for k, v in data.items()]


if __name__ == '__main__':
    solution = Solution().subdomainVisits(cpdomains=[
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org"])
    ic(solution)
