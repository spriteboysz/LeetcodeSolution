#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:25
FileName: algorithm/P1817. 查找用户活跃分钟数.py
Description: 
"""

from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = {}
        for id_, mm in logs:
            if id_ not in dic:
                dic[id_] = set()
            dic[id_].add(mm)

        dic2 = {}
        for key, v in dic.items():
            if len(v) not in dic2:
                dic2[len(v)] = 0
            dic2[len(v)] += 1
        actives = [0] * k
        for key, v in dic2.items():
            actives[key - 1] = v
        return actives


if __name__ == '__main__':
    solution = Solution().findingUsersActiveMinutes(logs=[[1,1],[2,2],[2,3]], k=4)
    print(solution)
