#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-30 20:22
FileName: P3407. 子字符串匹配模式
Description:
"""
import re

from icecream import ic


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pattern = p.replace('*', '.*')
        return bool(re.findall(pattern, s))


if __name__ == '__main__':
    solution = Solution().hasMatch(s="leetcode", p="ee*e")
    ic(solution)
