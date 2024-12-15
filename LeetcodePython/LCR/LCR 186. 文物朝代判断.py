#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:48
FileName: LCR 186. 文物朝代判断
Description:
"""
from typing import List


class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        places = [place for place in places if place > 0]
        return len(places) == len(set(places)) and max(places) - min(places) <= 4


if __name__ == '__main__':
    solution = Solution().checkDynasty(places=[0, 6, 9, 0, 7])
    print(solution)
