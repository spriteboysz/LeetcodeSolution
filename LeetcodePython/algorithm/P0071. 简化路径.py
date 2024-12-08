#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 22:31
FileName: P0071. 简化路径
Description:
"""
import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = re.split(r'/+', path)
        stack = []
        for p in paths:
            if p == '':
                continue
            if p == '.':
                pass
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return f'/{"/".join(stack)}'


if __name__ == '__main__':
    solution = Solution().simplifyPath(path="/home/user///Documents/../Pictures")
    print(solution)
