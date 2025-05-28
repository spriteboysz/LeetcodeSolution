#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-05-28 21:49
FileName: algorithm/P3484. 设计电子表格.py
Description: 
"""

from icecream import ic


class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    @staticmethod
    def _get_position(cell):
        return int(cell[1:]) - 1, ord(cell[0]) - ord('A')

    def _get_value(self, cell):
        if cell.isdigit():
            return int(cell)
        x, y = self._get_position(cell)
        return int(self.grid[x][y])

    def setCell(self, cell: str, value: int) -> None:
        x, y = self._get_position(cell)
        self.grid[x][y] = value

    def resetCell(self, cell: str) -> None:
        x, y = self._get_position(cell)
        self.grid[x][y] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        return self._get_value(a) + self._get_value(b)


if __name__ == '__main__':
    sheet = Spreadsheet(458)
    ic(sheet.getValue('=O126+10272'))
    sheet.setCell('A1', 10)
    ic(sheet.getValue('=A1+6'))
