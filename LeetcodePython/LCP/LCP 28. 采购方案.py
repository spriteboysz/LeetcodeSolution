#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 21:30
FileName: LCP 28. 采购方案
Description:
"""
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, cnt = 0, len(nums) - 1, 0
        while left < right:
            if nums[left] + nums[right] <= target:
                cnt += right - left
                left += 1
            else:
                right -= 1
        return cnt % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution().purchasePlans(nums=[2, 2, 2, 9], target=4)
    print(solution)
