#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 09:46
FileName: P0609. 在系统中查找重复文件.py
Description:
"""
from typing import List

from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            p, *files = path.split()
            for file in files:
                name, content = file.split('(')
                dic[content].append(f'{p}/{name}')
        return [v for v in dic.values() if len(v) > 1]



if __name__ == '__main__':
    solution = Solution().findDuplicate(
        paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
    print(solution)
