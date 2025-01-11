#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-11 21:44
FileName: P1773. 统计匹配检索规则的物品数量
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = ['type', 'color', 'name'].index(ruleKey)
        return sum(item[index] == ruleValue for item in items)


if __name__ == '__main__':
    solution = Solution().countMatches(
        items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
        ruleKey="type", ruleValue="phone")
    ic(solution)
