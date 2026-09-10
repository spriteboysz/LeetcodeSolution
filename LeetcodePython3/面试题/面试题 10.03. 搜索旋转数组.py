#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 08:48
FileName: 面试题/面试题 10.03. 搜索旋转数组.py
Description: 
"""
from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[left] < arr[mid]:
                if arr[left] <= target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] > arr[mid]:
                if arr[left] <= target or target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if arr[left] != target:
                    left += 1
                else:
                    right = left
        return left if arr[left] == target else -1


if __name__ == '__main__':
    solution = Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5)
    print('<None>' if not solution else f'{solution=}')
