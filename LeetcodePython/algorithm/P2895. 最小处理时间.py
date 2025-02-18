#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-18 23:05
FileName: P2895. 最小处理时间
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        return max(m + p for m, p in zip(tasks[::4], processorTime))


if __name__ == '__main__':
    solution = Solution().minProcessingTime(processorTime=[8, 10], tasks=[2, 2, 3, 1, 8, 7, 4, 5])
    ic(solution)
