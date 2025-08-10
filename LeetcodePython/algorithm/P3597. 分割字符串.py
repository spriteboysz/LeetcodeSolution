#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-08-10 11:14
FileName: algorithm/P3597. 分割字符串.py
Description: 
"""
from collections import OrderedDict
from typing import List

from icecream import ic


class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments, segment = OrderedDict(), ''
        for ch in s:
            segment += ch
            if segment not in segments:
                segments.update({segment: ''})
                segment = ''
        return list(segments)


if __name__ == '__main__':
    solution = Solution().partitionString(s="aaaa")
    ic(solution)
