#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-06 23:31
FileName: LCR 189. 设计机械累加器
Description:
"""

from icecream import ic


class Solution:
    def mechanicalAccumulator(self, target: int) -> int:
        if target == 1:
            return target
        return target + self.mechanicalAccumulator(target - 1)


if __name__ == '__main__':
    solution = Solution().mechanicalAccumulator(7)
    ic(solution)
