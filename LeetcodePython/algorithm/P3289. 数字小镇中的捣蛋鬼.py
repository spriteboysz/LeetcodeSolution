#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 21:55
FileName: P3289. 数字小镇中的捣蛋鬼
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return [k for k, v in dic.items() if v == 2]


if __name__ == '__main__':
    solution = Solution().getSneakyNumbers(nums=[0, 3, 2, 1, 3, 2])
    print(solution)
