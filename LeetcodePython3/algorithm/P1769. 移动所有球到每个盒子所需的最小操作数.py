#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 09:34
FileName: P1769. 移动所有球到每个盒子所需的最小操作数.py
Description:
"""
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations = []
        for i in range(len(boxes)):
            cnt = sum(abs(j - i) * int(boxes[j]) for j in range(len(boxes)))
            operations.append(cnt)
        return operations


if __name__ == '__main__':
    solution = Solution().minOperations(boxes="001011")
    print(solution)
