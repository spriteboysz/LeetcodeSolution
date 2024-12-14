#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 13:45
FileName: LCR 002. 二进制求和
Description:
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack1, stack2, carry = list(a), list(b), 0
        ans = []
        while stack1 or stack2 or carry:
            if stack1:
                carry += int(stack1.pop())
            if stack2:
                carry += int(stack2.pop())
            carry, mod = divmod(carry, 2)
            ans.append(mod)
        return ''.join(map(str, ans))[::-1]


if __name__ == '__main__':
    solution = Solution().addBinary(a="1111", b="1")
    print(solution)
