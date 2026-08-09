#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:03
FileName: P1720. 解码异或后的数组.py
Description:
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(num ^ decoded[-1])
        return decoded


if __name__ == '__main__':
    solution = Solution().decode(encoded=[1, 2, 3], first=1)
    print(solution)
