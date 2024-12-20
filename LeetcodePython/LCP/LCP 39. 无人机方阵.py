#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 21:13
FileName: LCP 39. 无人机方阵
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        nums1, nums2 = sum(source, []), sum(target, [])
        counter1, counter2 = Counter(nums1), Counter(nums2)
        cnt = 0
        for color in {*counter1, *counter2}:
            cnt += abs(counter1.get(color, 0) - counter2.get(color, 0))
        return cnt // 2


if __name__ == '__main__':
    solution = Solution().minimumSwitchingTimes(source=[[1, 3], [5, 4]], target=[[3, 1], [6, 5]])
    print(solution)
