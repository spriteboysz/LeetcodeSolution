#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-15 10:57
FileName: algorithm/P0703. 数据流中的第 K 大元素.py
Description: 
"""
import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.queue = nums
        heapq.heapify(self.queue)

    def add(self, val):
        heapq.heappush(self.queue, val)
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
        return self.queue[0]


if __name__ == '__main__':
    solution = KthLargest(3, [4, 5, 8, 2])
    print(solution.add(3))
    print(solution.add(5))
    print(solution.add(10))
    print(solution.add(9))
    print(solution.add(4))
