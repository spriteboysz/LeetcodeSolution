#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 21:36
FileName: P0832. 翻转图像
Description:
"""
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])
        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(m):
                image[i][j] = 1 - image[i][j]
        return image


if __name__ == '__main__':
    solution = Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
    print(solution)
