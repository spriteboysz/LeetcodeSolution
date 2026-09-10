#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 18:35
FileName: 面试题/LCR 059. 数据流中的第 K 大元素.py
Description: 
"""
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    solution = KthLargest(3, [4, 5, 8, 2])
    print(solution.add(3))
    print(solution.add(5))
    print(solution.add(10))
    print(solution.add(9))
    print(solution.add(4))
