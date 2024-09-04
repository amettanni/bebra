import asyncio
import random
from typing import Callable
from loguru import logger

from utils.modules import *
from utils.utils import async_sleep, remove_wallet_from_files
from settings import MainSettings as SETTINGS
from utils.wrappers import repeats


async def start_tasks(data: list, module: Callable = None):
    while True:
        for account in data:
            await run_main_proccesses(account.get('id'), account.get('key'), module)

        if SETTINGS.INFINITE_MODE == False:
            break


async def run_main_proccesses(account_id: int, key: str, module: Callable = None):
    # ignore for the first wallet
    if account_id > 1 and module is None:
        await async_sleep(
            SETTINGS.START_PERIOD[0], SETTINGS.START_PERIOD[1],
            True, account_id, key, 'before starting work'
        )
    
    if module:
        await run_module(module, account_id, key)
    else:
        if not SETTINGS.CUSTOM_ROUTES_MODULES:
            raise ValueError(f'Enter your modules to CUSTOM_ROUTES_MODULES in the settings.')
        
        choiced_route = random.choice(SETTINGS.CUSTOM_ROUTES_MODULES)
        for module in choiced_route:
            if not module: continue
            
            await run_module(eval(module), account_id, key)


@repeats
async def run_module(module: Callable, account_id: int, key: str):
    succcess_bridge = await module(account_id, key)
    if not succcess_bridge: return False
    return True