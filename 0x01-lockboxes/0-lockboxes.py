#!/usr/bin/env python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from box 0.

    Args:
        boxes (list of list of int): A list of lists where each inner list represents the keys in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Mark the initial box as visited
    stack = [0]  # Initialize a stack with the initial box

    while stack:
        current_box = stack.pop()  # Get the top box from the stack
        keys = boxes[current_box]  # Get the keys in the current box

        for key in keys:
            if key not in visited:
                visited.add(key)  # Mark the box as visited
                stack.append(key)  # Add the box to the stack

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
