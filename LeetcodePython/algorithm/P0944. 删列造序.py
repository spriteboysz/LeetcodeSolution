#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 20:47
FileName: P0944. 删列造序
Description:
"""
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(sorted(list(el)) != list(el) for el in zip(*strs))


if __name__ == '__main__':
    solution = Solution().minDeletionSize(["zyx", "wvu", "tsr"])
    print(solution)
