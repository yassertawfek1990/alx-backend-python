#!/usr/bin/env python3
""" f f f."""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ df ff"""
    for sddsd in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
