#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-05 23:53
FileName: P0071. 简化路径.py
Description:
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [p for p in path.split('/') if p and p != '.']
        stack = []
        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    solution = Solution().simplifyPath(path="/home//user/./Documents/../Pictures")
    print(solution)
