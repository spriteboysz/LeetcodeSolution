#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-29 23:13
FileName: P3921. 分数验证器.py
Description:
"""


class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for event in events:
            if event == 'W':
                counter += 1
            elif event in ['WD', 'NB']:
                score += 1
            else:
                score += int(event)
            if counter == 10:
                break
        return [score, counter]


if __name__ == '__main__':
    solution = Solution().scoreValidator(events=["1", "4", "W", "6", "WD"])
    print(solution)
