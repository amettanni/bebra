import asyncio
import sys
from loguru import logger
from web3 import Web3

from settings import MainSettings as SETTINGS
from utils.utils import async_sleep



def repeats(func):
    async def wrapper(*args, **kwargs):
        if SETTINGS.REPEATS_PER_WALLET == 0:
            logger.error(f'The "MODULE_REPEATS" parameter cannot be equal to 0.')
            sys.exit()
        
        current_repeat = 0

        while current_repeat < SETTINGS.REPEATS_PER_WALLET:
            success = await func(*args, **kwargs)

            current_repeat += 1

            if not success or current_repeat == SETTINGS.REPEATS_PER_WALLET:
                break
            
            await async_sleep(
                SETTINGS.SLEEP_AFTER_WORK_FROM,
                SETTINGS.SLEEP_AFTER_WORK_TO,
                account_id=args[1],
                key=args[2]
            )

    return wrapper