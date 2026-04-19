#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-19 20:29
FileName: P3354. 使数组元素等于零.py
Description:
"""
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def move(index, bound):
            """
            移动
            :param index: 数字索引
            :param bound: 方向，右为1，左为-1
            :return: 全0返回1，否则返回0
            """
            arr = nums.copy()
            while 0 <= index < len(arr):
                if arr[index] > 0:
                    arr[index] -= 1
                    bound = - bound
                index += bound
            return int(all(el == 0 for el in arr))

        return sum(move(i, 1) + move(i, -1) for i, num in enumerate(nums) if num == 0)


if __name__ == '__main__':
    solution = Solution().countValidSelections(nums=[16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7])
    print(solution)
