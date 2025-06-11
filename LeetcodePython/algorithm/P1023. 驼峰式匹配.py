#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-10 23:32
FileName: algorithm/P1023. 驼峰式匹配.py
Description: 
"""
import re
from typing import List

from icecream import ic


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pat = '^[a-z]*' + '[a-z]*'.join(list(pattern)) + '[a-z]*$'
        return [bool(re.findall(pat, query)) for query in queries]


if __name__ == '__main__':
    solution = Solution().camelMatch(
        queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        pattern="FoBaT"
    )
    ic(solution)
