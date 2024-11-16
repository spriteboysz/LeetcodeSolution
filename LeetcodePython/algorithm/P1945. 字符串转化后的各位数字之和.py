#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 18:14
FileName: P1945. 字符串转化后的各位数字之和
Description:
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''.join(map(str, [ord(ch) - ord('a') + 1 for ch in s]))
        while k > 0:
            ss = str(sum(map(int, list(ss))))
            k -= 1
        return int(ss)


if __name__ == '__main__':
    solution = Solution().getLucky('leetcode', 2)
    print(solution)
