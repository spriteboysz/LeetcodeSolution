#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-09 23:12
FileName: P2678. 老人的数目.py
Description:
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[-4:-2]) > 60 for detail in details)


if __name__ == '__main__':
    solution = Solution().countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"])
    print(solution)
