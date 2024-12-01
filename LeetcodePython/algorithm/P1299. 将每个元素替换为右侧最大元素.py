#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 21:54
FileName: P1299. 将每个元素替换为右侧最大元素
Description:
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        nums = []
        for num in arr[::-1]:
            nums.append(maximum)
            maximum = max(maximum, num)
        return nums[::-1]


if __name__ == '__main__':
    solution = Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1])
    print(solution)
