#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-20 22:52
FileName: algorithm/P0609. 在系统中查找重复文件.py
Description: 
"""
from typing import List
from collections import defaultdict

from icecream import ic


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(set)
        for path in paths:
            ss = path.split()
            for file in ss[1:]:
                filename, content = file.split('(')
                dic[content[:-1]].add(f'{ss[0]}/{filename}')
        return [list(path) for path in dic.values() if len(path) > 1]


if __name__ == '__main__':
    solution = Solution().findDuplicate(
        paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
    ic(solution)
