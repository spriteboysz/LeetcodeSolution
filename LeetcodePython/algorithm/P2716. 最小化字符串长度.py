#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 22:41
FileName: P2716. 最小化字符串长度
Description:
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ss, seen = [], set()
        for ch in s:
            if ch not in seen:
                ss.append(ch)
                seen.add(ch)
        return len(ss)



if __name__ == '__main__':
    solution = Solution().minimizedStringLength(s="aaabc")
    print(solution)
