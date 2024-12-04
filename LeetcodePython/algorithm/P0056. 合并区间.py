#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 21:41
FileName: P0056. 合并区间
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret, curr, left = [], 0, 0
        dic = defaultdict(int)
        for start, end in intervals:
            dic[start] += 1
            dic[end] -= 1
        for i in sorted(dic):
            if curr == 0:
                left = i
            curr += dic[i]
            if curr == 0:
                ret.append([left, i])
        return ret


if __name__ == '__main__':
    solution = Solution().merge([[1, 4], [0, 0]])
    print(solution)
