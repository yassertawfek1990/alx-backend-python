#!/usr/bin/env python3
""" Imposdrt wasd"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Lesd sd"""
    delays: List[float] = []
    all_delays: List[float] = []
    for ff in range(n):
        delays.append(wait_random(max_delay))
    for yy in asyncio.as_completed(delays):
        er = await yy
        all_delays.append(er)
    return all_delay
