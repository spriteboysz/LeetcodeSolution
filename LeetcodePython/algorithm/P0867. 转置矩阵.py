#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:32
FileName: P0867. 转置矩阵
Description:
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(lambda el: list(el), zip(*matrix)))


if __name__ == '__main__':
    solution = Solution().transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(solution)
