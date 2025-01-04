#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 17:20
FileName: P0869. 重新排序得到 2 的幂
Description:
"""

from icecream import ic

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        targets = (''.join(sorted(list(str(2 ** i)))) for i in range(32))
        for target in targets:
            if ''.join(sorted(list(str(n)))) == target:
                return True
        return False


if __name__ == '__main__':
    solution = Solution().reorderedPowerOf2(61)
    ic(solution)
