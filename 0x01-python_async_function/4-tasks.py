#!/usr/bin/env python3
""" Take tsc ds. """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Vsdc """
    delays: List[float] = []
    all_delays: List[float] = []
    for dd in range(n):
        delays.append(task_wait_random(max_delay))
    for ff in asyncio.as_completed(delays):
        v = await ff
        all_delays.append(v)
    return all_delays
