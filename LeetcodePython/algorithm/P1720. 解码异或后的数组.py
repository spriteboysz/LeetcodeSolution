#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-06 23:28
FileName: P1720. 解码异或后的数组
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(decoded[-1] ^ num)
        return decoded


if __name__ == '__main__':
    solution = Solution().decode(encoded=[1, 2, 3], first=1)
    ic(solution)
