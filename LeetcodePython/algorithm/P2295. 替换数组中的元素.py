#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 21:33
FileName: P2295. 替换数组中的元素
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num: num for num in set(nums)}
        for a, b in operations:
            dic.update({b: dic[a]})
            dic.pop(a)
        dic = {v: k for k, v in dic.items()}
        return [dic[num] for num in nums]


if __name__ == '__main__':
    solution = Solution().arrayChange(nums=[1, 2, 4, 6], operations=[[1, 3], [4, 7], [6, 1]])
    ic(solution)
