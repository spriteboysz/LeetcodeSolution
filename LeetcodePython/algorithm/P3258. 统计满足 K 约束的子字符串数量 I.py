#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-12 23:17
FileName: P3258. 统计满足 K 约束的子字符串数量 I
Description:
"""


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = 0
        for i in range(n:=len(s)):
            for j in range(i, n):
                ss = s[i:j + 1]
                if ss.count('0') <= k or ss.count('1') <= k:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countKConstraintSubstrings(s="10101", k=1)
    print(solution)
