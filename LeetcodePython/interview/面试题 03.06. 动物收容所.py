#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 17:25
FileName: interview/面试题 03.06. 动物收容所.py
Description: 
"""
from collections import deque
from typing import List

from icecream import ic


class AnimalShelf:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, animal: List[int]) -> None:
        self.queue.append(animal)

    def dequeueAny(self) -> List[int]:
        if self.queue:
            return self.queue.popleft()
        return [-1, -1]

    def dequeueDog(self) -> List[int]:
        for i in range(len(self.queue)):
            if self.queue[i][1] == 1:
                animal = self.queue[i]
                del self.queue[i]
                return animal
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        for i in range(len(self.queue)):
            if self.queue[i][1] == 0:
                animal = self.queue[i]
                del self.queue[i]
                return animal
        return [-1, -1]


if __name__ == '__main__':
    animals = AnimalShelf()
    animals.enqueue([0, 0])
    animals.enqueue([1, 0])
    ic(animals.dequeueAny())
    ic(animals.dequeueDog())
    ic(animals.dequeueCat())
