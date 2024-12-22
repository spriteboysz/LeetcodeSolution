#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 20:08
FileName: 面试题 17.10. 主要元素
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = [num for num, cnt in counter.items() if cnt > len(nums) // 2]
        return majority[0] if majority else -1


if __name__ == '__main__':
    solution = Solution().majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])
    print(solution)
