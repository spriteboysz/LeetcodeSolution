#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 17:39
FileName: algorithm/P1146. 快照数组.py
Description: 
"""
from bisect import bisect_left
from collections import defaultdict

from icecream import ic


class SnapshotArray:
    def __init__(self, _: int):
        self.cur_snap_id = 0
        self.history = defaultdict(list)  # 每个 index 的历史修改记录

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 找快照编号 <= snap_id 的最后一次修改记录
        # 等价于找快照编号 >= snap_id+1 的第一个修改记录，它的上一个就是答案
        j = bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][j][1] if j >= 0 else 0


if __name__ == '__main__':
    snapshot = SnapshotArray(3)
    snapshot.set(0, 5)
    ic(snapshot.snap())
    snapshot.set(0, 7)
    ic(snapshot.get(0, 0))
