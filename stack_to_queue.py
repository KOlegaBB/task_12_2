"""
Stack to queue converter.
"""

from arrayqueue import ArrayQueue
from copy import deepcopy


def stack_to_queue(stack):
    """
    Create queue from stack
    """
    queue = ArrayQueue()
    new_stack = deepcopy(stack)
    for _ in range(len(new_stack)):
        queue.add(new_stack.pop())
    return queue
