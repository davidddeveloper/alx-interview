#!/usr/bin/env python3
"""
  0-lockboxes: represent a lockboxes solution with loops

"""

def canUnlockAll(boxes):
    """ True if all boexes can be opened

        False otherwise
    """
    viewedboxes = {0}  # keys of boxes
    for idx, val in enumerate(boxes):
        if idx not in viewedboxes and idx > 0:
            for key in val:
                viewedboxes.add(key)

    if len(viewedboxes) == len(boxes):
        return True
    return False
