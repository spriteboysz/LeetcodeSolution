#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 14:26
FileName: LCR 172. 统计目标成绩的出现次数
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        counter = Counter(scores)
        return counter.get(target, 0)


if __name__ == '__main__':
    solution = Solution().countTarget(scores=[2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target=4)
    print(solution)
