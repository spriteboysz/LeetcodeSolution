#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:28
FileName: P2011. 执行操作后的变量值
Description:
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for operation in operations:
            if '+' in operation:
                value += 1
            else:
                value -= 1
        return value


if __name__ == '__main__':
    solution = Solution().finalValueAfterOperations(operations=["--X", "X++", "X++"])
    print(solution)
