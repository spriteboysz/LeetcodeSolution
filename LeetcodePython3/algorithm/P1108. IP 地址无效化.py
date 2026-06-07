#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 17:13
FileName: P1108. IP 地址无效化.py
Description:
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    solution = Solution().defangIPaddr('1.1.1.1')
    print(solution)
