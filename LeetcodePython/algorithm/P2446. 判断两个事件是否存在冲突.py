#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-25 12:04
FileName: P2446. 判断两个事件是否存在冲突
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def process(events):
            tt = []
            for event in events:
                hh, mm = event.split(':')
                tt.append(int(hh) * 60 + int(mm))
            return tt

        s1, e1, s2, e2 = process([*event1, *event2])
        return s1 <= e2 and e1 >= s2


if __name__ == '__main__':
    solution = Solution().haveConflict(event1=["01:15", "02:00"], event2=["02:00", "03:00"])
    ic(solution)
