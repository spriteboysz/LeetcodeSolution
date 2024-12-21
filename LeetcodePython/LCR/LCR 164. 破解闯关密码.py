#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 11:51
FileName: LCR 164. 破解闯关密码
Description:
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        return ''.join(sorted(map(str, password), key=cmp_to_key(lambda x, y: int(x + y) - int(y + x))))


if __name__ == '__main__':
    solution = Solution().crackPassword(password=[0, 3, 30, 34, 5, 9])
    print(solution)
