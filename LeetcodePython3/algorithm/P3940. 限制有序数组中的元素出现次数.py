#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:20
FileName: P3940. 限制有序数组中的元素出现次数.py
Description:
"""


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > k:
                nums[i - 1] = 0
        return [num for num in nums if num]


if __name__ == '__main__':
    solution = Solution().limitOccurrences(nums=[40, 40, 40], k=1)
    print(solution)
