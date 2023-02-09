#!/usr/bin/env python3
"""
a function (do not create an async function, use the regular
function syntax to do this) task_wait_random
"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Tasks """
    task = create_task(wait_random(max_delay))
    return task
