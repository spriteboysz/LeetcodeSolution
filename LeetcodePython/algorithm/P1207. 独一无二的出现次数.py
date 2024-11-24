#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 14:17
FileName: P1207. 独一无二的出现次数
Description:
"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = list(Counter(arr).values())
        return len(counter) == len(set(counter))


if __name__ == '__main__':
    solution = Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])
    print(solution)