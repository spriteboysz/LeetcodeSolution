#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-09 23:33
FileName: P0347. 前 K 个高频元素
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        frequent = sorted([(num, cnt) for num, cnt in dic.items()], key=lambda el: el[1], reverse=True)
        return [num for num, _ in frequent[:k]]


if __name__ == '__main__':
    solution = Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
    print(solution)
