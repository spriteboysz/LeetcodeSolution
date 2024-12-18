#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-18 22:59
FileName: P1046. 最后一块石头的重量
Description:
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -abs(a - b))
        return -heap[0] if heap else 0


if __name__ == '__main__':
    solution = Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
    print(solution)
