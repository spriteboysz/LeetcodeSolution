#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 21:44
FileName: P1356. 根据数字二进制下 1 的数目排序
Description:
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda el: (el.bit_count(), el))
        return arr


if __name__ == '__main__':
    solution = Solution().sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(solution)
