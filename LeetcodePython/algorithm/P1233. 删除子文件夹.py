#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 10:10
FileName: algorithm/P1233. 删除子文件夹.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        for i in range(len(folder)):
            index = []
            for j in range(i + 1, len(folder)):
                if folder[j].startswith(folder[i] + '/'):
                    index.append(j)
                else:
                    break
            folder = [f for k, f in enumerate(folder) if k not in index]
        return folder


if __name__ == '__main__':
    solution = Solution().removeSubfolders(folder=["/a", "/c/d", "/a/b", "/c/d/e", "/c/f"])
    ic(solution)
