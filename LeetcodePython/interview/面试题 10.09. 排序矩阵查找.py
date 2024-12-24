#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 23:01
FileName: 面试题 10.09. 排序矩阵查找
Description:
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            for num in row:
                if num == target:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution().searchMatrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]], 5)
    print(solution)
