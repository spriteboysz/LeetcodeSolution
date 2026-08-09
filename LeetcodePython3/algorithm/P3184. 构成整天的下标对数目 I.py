#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:46
FileName: P3184. 构成整天的下标对数目 I.py
Description:
"""
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = 0
        for i, hour1 in enumerate(hours):
            for hour2 in hours[i + 1:]:
                if (hour1 + hour2) % 24 == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countCompleteDayPairs(hours=[12, 12, 30, 24, 24])
    print(solution)
