#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 12:15
FileName: P1108. IP 地址无效化
Description:
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

if __name__ == '__main__':
    solution = Solution().defangIPaddr('1.1.1.1')
    print(solution)