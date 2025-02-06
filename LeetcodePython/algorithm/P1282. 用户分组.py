#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-04 12:59
FileName: P1282. 用户分组
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        for i, group in enumerate(groupSizes):
            dic[group].append(i)
        return [v[i:i + k] for k, v in dic.items() for i in range(0, len(v), k)]


if __name__ == '__main__':
    solution = Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3])
    ic(solution)
