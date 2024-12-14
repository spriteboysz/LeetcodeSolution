#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 11:41
FileName: LCR 135. 报数
Description:
"""
from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        return list(range(1, 10 ** cnt))


if __name__ == '__main__':
    solution = Solution().countNumbers(2)
    print(solution)
