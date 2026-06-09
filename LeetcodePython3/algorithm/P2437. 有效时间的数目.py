#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:20
FileName: P2437. 有效时间的数目.py
Description:
"""


class Solution:
    def countTime(self, time: str) -> int:
        cnt = 0
        for i in range(24 * 60):
            hh, mm = divmod(i, 60)
            curr = f'{hh:02d}:{mm:02d}'
            if all(time[j] == '?' for j in range(5) if time[j] != curr[j]):
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countTime(time="0?:0?")
    print(solution)
