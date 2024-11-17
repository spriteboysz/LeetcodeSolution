#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 20:05
FileName: P1323. 6 和 9 组成的最大数字
Description:
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    solution = Solution().maximum69Number(9669)
    print(solution)
