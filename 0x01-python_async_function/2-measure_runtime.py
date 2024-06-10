#!/usr/bin/env python3
""" Srom ds """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Me sd"""
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    e = time.time()
    total_time = e - s
    return total_time / n
