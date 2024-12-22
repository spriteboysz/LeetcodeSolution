#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 20:24
FileName: 面试题 01.06. 字符串压缩
Description:
"""


class Solution:
    def compressString(self, s: str) -> str:
        if not s:
            return s
        ss, curr = '', 1
        for i in range(1, len(s) + 1):
            if i < len(s) and s[i - 1] == s[i]:
                curr += 1
            else:
                ss += f'{s[i - 1]}{curr}'
                curr = 1
        return ss if len(ss) < len(s) else s


if __name__ == '__main__':
    solution = Solution().compressString("abbccd")
    print(solution)
