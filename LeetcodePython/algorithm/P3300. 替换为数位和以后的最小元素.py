#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-21 23:20
FileName: P3300. 替换为数位和以后的最小元素
Description:
"""
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(map(lambda el: sum(map(int, str(el))), nums))


if __name__ == '__main__':
    solution = Solution().minElement(nums=[999, 19, 199])
    print(solution)
