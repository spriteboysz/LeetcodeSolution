#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 22:57
FileName: P0137. 只出现一次的数字 II
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for num, cnt in dic.items():
            if cnt == 1:
                return num
        return -1


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99])
    print(solution)
