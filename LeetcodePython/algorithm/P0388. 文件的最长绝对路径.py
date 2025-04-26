#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 9:36
FileName: algorithm/P0388. 文件的最长绝对路径.py
Description: 
"""

from icecream import ic


class Solution:
    def lengthLongestPath(self, paths: str) -> int:
        curr, files = [], []
        for path in paths.split('\n'):
            content = path.lstrip('\t')
            level = len(path) - len(content)
            curr = curr[:level]
            curr.append(content)
            if '.' in content:
                files.append('/'.join(curr))
        return max([len(file) for file in files]) if files else 0


if __name__ == '__main__':
    solution = Solution().lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    ic(solution)
