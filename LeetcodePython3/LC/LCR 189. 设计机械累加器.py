#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-31 22:58
FileName: LCR/LCR 189. 设计机械累加器.py
Description: 
"""


class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        if target == 1:
            return target
        return target + self.mechanicalAccumulator(target - 1)


if __name__ == '__main__':
    solution = Solution().mechanicalAccumulator(7)
    print(solution)
