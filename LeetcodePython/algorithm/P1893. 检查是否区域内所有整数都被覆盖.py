#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-26 23:06
FileName: P1893. 检查是否区域内所有整数都被覆盖
Description:
"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = [0] * 51
        for s, e in ranges:
            nums[s:e + 1] = [1] * (e - s + 1)
        return all([nums[i] == 1 for i in range(left, right + 1)])


if __name__ == '__main__':
    solution = Solution().isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5)
    print(solution)
