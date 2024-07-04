#!/usr/bin/python3
"""
Lockbox
"""
from collections import deque


def canUnlockAll(boxes):
    """
    unlockable
    """

    n = len(boxes)
    if n == 0:
        return True

    visitedList = [False] * n
    visitedList[0] = True
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key < n and not visitedList[key]:
                visitedList[key] = True
                queue.append(key)

    return all(visitedList)
