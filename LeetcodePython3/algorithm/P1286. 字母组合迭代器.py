#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-15 10:24
FileName: algorithm/P1286. 字母组合迭代器.py
Description: 
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        path = []
        self.queue = []

        def dfs(i):
            if len(path) == combinationLength:
                self.queue.append(''.join(path))
                return
            for j in range(i, len(characters)):
                path.append(characters[j])
                dfs(j + 1)
                path.pop()

        dfs(0)

    def next(self) -> str:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return bool(self.queue)


if __name__ == '__main__':
    solution = CombinationIterator('abc', 2)
    print(solution.next())
    print(solution.hasNext())
    print(solution.next())
    print(solution.hasNext())
    print(solution.next())
    print(solution.hasNext())
