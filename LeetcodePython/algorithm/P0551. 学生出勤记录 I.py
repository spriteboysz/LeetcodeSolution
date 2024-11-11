#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 22:56
FileName: P0551. 学生出勤记录 I
Description:
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s

if __name__ == '__main__':
    solution = Solution().checkRecord(s = "PPALLP")
    print(solution)