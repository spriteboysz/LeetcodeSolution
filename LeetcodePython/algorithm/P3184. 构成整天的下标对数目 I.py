#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 20:38
FileName: P3184. 构成整天的下标对数目 I
Description:
"""
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = 0
        for i, hour1 in enumerate(hours):
            for hour2 in hours[:i]:
                if (hour1 + hour2) % 24 == 0:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countCompleteDayPairs(hours=[72, 48, 24, 3])
    print(solution)
