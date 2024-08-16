#!/usr/bin/env python3
"""
lockboxes
"""


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked starting from box 0.

    Args:
        boxes (List[List[int]]): A list of lists where each inner
                                 list represents the keys in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()
    queue = [0]  # Start with box 0

    while queue:
        box = queue.pop(0)
        if box in visited:
            continue
        visited.add(box)
        for key in boxes[box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
