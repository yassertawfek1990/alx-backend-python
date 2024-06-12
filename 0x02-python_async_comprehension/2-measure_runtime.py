#!/usr/bin/env python3
""" Dvd fdf g."""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ dvsdv dv v."""
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for vvvv in range(4)))
    end: float = time.perf_counter()
    return (end - start)
