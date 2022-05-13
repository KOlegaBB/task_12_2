"""
Queue to stack converter.
"""

from arraystack import ArrayStack
from copy import deepcopy


def queue_to_stack(queue):
    """
    Create stack from queue
    """
    stack = ArrayStack()
    new_queue = deepcopy(queue)
    length = len(new_queue)
    for iterator in range(length):
        stack.add(new_queue.peek())
        new_queue.remove(length - iterator - 1)
    return stack
