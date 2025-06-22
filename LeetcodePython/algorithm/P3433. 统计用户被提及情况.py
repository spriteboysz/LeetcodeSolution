#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-15 22:34
FileName: algorithm/P3433. 统计用户被提及情况.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), e[0][2]))
        mentions = [0] * numberOfUsers
        online_t = [0] * numberOfUsers
        for msg, stamp, mention in events:
            curr = int(stamp)
            if msg == 'OFFLINE':
                online_t[int(mention)] = curr + 60
            elif mention == 'ALL':
                for i in range(numberOfUsers):
                    mentions[i] += 1
            elif mention == 'HERE':
                for i, t in enumerate(online_t):
                    if t <= curr:
                        mentions[i] += 1
            else:
                for s in mention.split():
                    mentions[int(s[2:])] += 1
        return mentions


if __name__ == '__main__':
    solution = Solution().countMentions(
        numberOfUsers=2,
        events=[["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]
    )
    ic(solution)
