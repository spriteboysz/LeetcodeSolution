#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-04 21:06
FileName: algorithm/P1472. 设计浏览器历史记录.py
Description: 
"""

from icecream import ic


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.position = 0

    def visit(self, url: str) -> None:
        self.position += 1
        del self.history[self.position:]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.position = max(self.position - steps, 0)
        return self.history[self.position]

    def forward(self, steps: int) -> str:
        self.position = min(self.position + steps, len(self.history) - 1)
        return self.history[self.position]


if __name__ == '__main__':
    browse_history = BrowserHistory('leetcode.com')
    browse_history.visit('google.com')
    browse_history.visit('facebook.com')
    browse_history.visit('facebook.com')
    ic(browse_history.back(1))
    ic(browse_history.back(1))
    ic(browse_history.forward(1))
    browse_history.visit('linkedin.com')
    ic(browse_history.forward(2))
    ic(browse_history.back(2))
    ic(browse_history.back(7))
