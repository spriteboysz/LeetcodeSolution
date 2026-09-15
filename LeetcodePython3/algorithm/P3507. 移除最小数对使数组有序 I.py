#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 15:44
FileName: algorithm/P3507. 移除最小数对使数组有序 I.py
Description: 
"""
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(arr):
            return all(arr[k - 1] <= arr[k] for k in range(1, len(arr)))

        cnt = 0
        while not check(nums):
            minimum = nums[0] + nums[1]
            for i in range(2, len(nums)):
                minimum = min(nums[i - 1] + nums[i], minimum)
            for i in range(1, len(nums)):
                if nums[i - 1] + nums[i] == minimum:
                    nums[i - 1] += nums[i]
                    nums[i] = -50001
                    break
            nums = [num for num in nums if num != -50001]
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().minimumPairRemoval([5, 2, 3, 1])
    print('<None>' if solution is None else f'{solution=}')
