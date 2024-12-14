#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:27
FileName: LCR 120. 寻找文件副本
Description:
"""
from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        seen = set()
        for document in documents:
            if document in seen:
                return document
            seen.add(document)
        return -1


if __name__ == '__main__':
    solution = Solution().findRepeatDocument(documents=[2, 5, 3, 0, 5, 0])
    print(solution)
