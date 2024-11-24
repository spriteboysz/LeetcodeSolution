#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 13:02
FileName: P2437. 有效时间的数目
Description:
"""


class Solution:
    def countTime(self, time: str) -> int:
        cnt = 0
        for i in range(24 * 60):
            hh, mm = divmod(i, 60)
            curr = f'{hh:02d}:{mm:02d}'
            for ch1, ch2 in zip(curr, time):
                if ch2 != '?' and ch1 != ch2:
                    break
            else:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countTime(time="?5:00")
    print(solution)
