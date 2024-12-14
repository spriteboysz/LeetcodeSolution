#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:13
FileName: LCR 182. 动态口令
Description:
"""


class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target:] + password[:target]


if __name__ == '__main__':
    solution = Solution().dynamicPassword(password="s3cur1tyC0d3", target=4)
    print(solution)
