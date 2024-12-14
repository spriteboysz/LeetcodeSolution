#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:58
FileName: P3159. 查询数组中元素的出现位置
Description:
"""
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        index = [i for i, num in enumerate(nums) if num == x]
        ans = []
        for query in queries:
            if query > len(index):
                ans.append(-1)
            else:
                ans.append(index[query - 1])
        return ans


if __name__ == '__main__':
    solution = Solution().occurrencesOfElement(nums=[1, 3, 1, 7], queries=[1, 3, 2, 4], x=1)
    print(solution)
