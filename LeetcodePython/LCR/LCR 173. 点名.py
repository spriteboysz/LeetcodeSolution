#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 10:02
FileName: LCR 173. 点名
Description:
"""
from typing import List


class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        return len(records) * (len(records) + 1) // 2 - sum(records)


if __name__ == '__main__':
    solution = Solution().takeAttendance(records=[0, 1, 2, 3, 4, 5, 6, 8])
    print(solution)
