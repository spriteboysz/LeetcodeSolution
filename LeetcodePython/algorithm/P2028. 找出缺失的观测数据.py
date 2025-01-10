#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-10 21:35
FileName: P2028. 找出缺失的观测数据
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        div, mod = divmod(mean * (len(rolls) + n) - sum(rolls), n)
        missing = [div + (i < mod) for i in range(n)]
        if max(missing) > 6 or min(missing) < 1:
            return []
        return missing


if __name__ == '__main__':
    solution = Solution().missingRolls(rolls=[1, 5, 6], mean=3, n=4)
    ic(solution)
