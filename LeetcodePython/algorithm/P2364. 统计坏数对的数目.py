#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 13:07
FileName: P2364. 统计坏数对的数目
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter()
        ans = n * (n - 1) // 2
        for i, num in enumerate(nums):
            ans -= cnt[num - i]
            cnt[num - i] += 1
        return ans


if __name__ == '__main__':
    solution = Solution().countBadPairs(nums=[4, 1, 3, 3])
    ic(solution)
