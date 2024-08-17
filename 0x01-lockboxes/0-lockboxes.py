#!/usr/bin/python3
"""Lockbox module"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists, where each sublist represents
                      a box and contains the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """

    # Initialize a list of unlocked boxes
    unlocked = [False] * len(boxes)
    # Set the first box open
    unlocked[0] = True

    # Iterate over the boxes
    for index, box in enumerate(boxes):
        # Check if the box is unlocked
        if unlocked[index]:
            # Get the keys in the box
            for key in box:
                # Set the box with a found key to open
                if key < len(unlocked):
                    unlocked[key] = True
                    # Get the keys at the box that has been opened
                    # Set the boxes with the keys to be open
                    for i in boxes[key]:
                        if i < len(unlocked):
                            unlocked[i] = True

    return all(unlocked)
