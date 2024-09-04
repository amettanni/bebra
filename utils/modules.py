import random
from settings import ModulesSettings as ms
from settings import MainSettings
from modules.modules.bend import Bend
from modules.modules.berps_pool import BerpsPool
from modules.modules.bex import Bex
from modules.modules.faucet import Faucet
from modules.account import Account
from utils.utils import async_sleep
from utils.config import BEX_POOLS


async def mint_berachain_tokens(account_id, key):
    account = Account(account_id, key, use_proxy=True)
    worker = Faucet(account)
    if worker.check_faucet_allowance():
        return await worker.claim_berachain_tokens()
    else:
        await async_sleep(
            MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1], 
            True, account.account_id, account.private_key, 'less than 8 hours from previous $BERA claiming'
        )


async def low_swap_bera_to_random_coin(account_id, key):
    min_percent = ms.Bex.LOW_PERCENTS[0]
    max_percent = ms.Bex.LOW_PERCENTS[1]
    coin = random.choice(list(BEX_POOLS.keys()))

    bex = Bex(account_id, key)
    await bex.swap_bera_to_coin(min_percent, max_percent, coin)


async def swap_bera_wbtc(account_id, key):
    min_percent = ms.Bex.PERCENTS[0]
    max_percent = ms.Bex.PERCENTS[1]

    bex = Bex(account_id, key)
    await bex.swap_bera_to_coin(min_percent, max_percent)


async def swap_bera_weth(account_id, key):
    min_percent = ms.Bex.PERCENTS[0]
    max_percent = ms.Bex.PERCENTS[1]

    bex = Bex(account_id, key)
    await bex.swap_bera_to_coin(min_percent, max_percent, coin="WETH")


async def swap_bera_honey(account_id, key):
    min_percent = ms.Bex.PERCENTS[0]
    max_percent = ms.Bex.PERCENTS[1]

    bex = Bex(account_id, key)
    await bex.swap_bera_to_coin(min_percent, max_percent, coin="HONEY")


async def bend_supply_wbtc_and_borrow_honey(account_id, key):
    # 2 actions in 1 function because they are all tied 
    # and should be done right one after another

    min_percent = ms.Bend.PERCENTS[0]
    max_percent = ms.Bend.PERCENTS[1]

    bend = Bend(account_id, key)

    approve_result = await bend.approve_wbtc()
    if approve_result:
        await async_sleep(
            MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
            True, account_id, key, 'before supplying WBTC to the Bend Pool'
        )
        supply_result = await bend.supply_wbtc(min_percent, max_percent)
        if supply_result:
            await async_sleep(
                MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
                True, account_id, key, 'before borrowing HONEY from the Bend Pool'
            )
            await bend.borrow_honey()


async def bend_supply_weth_and_borrow_honey(account_id, key):
    # 2 actions in 1 function because they are all tied 
    # and should be done right one after another

    min_percent = ms.Bend.PERCENTS[0]
    max_percent = ms.Bend.PERCENTS[1]

    bend = Bend(account_id, key)

    approve_result = await bend.approve_weth()
    if approve_result:
        await async_sleep(
            MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
            True, account_id, key, 'before supplying WETH to the Bend Pool'
        )
        supply_result = await bend.supply_weth(min_percent, max_percent)
        if supply_result:
            await async_sleep(
                MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
                True, account_id, key, 'before borrowing HONEY from the Bend Pool'
            )
            await bend.borrow_honey()


async def bend_get_reward(account_id, key):

    bend = Bend(account_id, key)
    await bend.get_reward_BGT()


async def berps_pool_deposit(account_id, key):

    min_percent = ms.BerpsPool.PERCENTS[0]
    max_percent = ms.BerpsPool.PERCENTS[1]

    berpsPool = BerpsPool(account_id, key)

    approve_honey_res = await berpsPool.approve_honey()
    if approve_honey_res:
        await async_sleep(
            MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
            True, account_id, key, 'before depositing HONEY to the Berps Pool'
        )
        deposit_honey_res = await berpsPool.deposit_honey(min_percent, max_percent)
        if deposit_honey_res:
            await async_sleep(
                MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
                True, account_id, key, 'before approving bHONEY'
            )
            approve_bhoney_res = await berpsPool.approve_bhoney()
            if approve_bhoney_res:
                await async_sleep(
                    MainSettings.SLEEP_INSIDE_MODULE[0], MainSettings.SLEEP_INSIDE_MODULE[1],
                    True, account_id, key, 'before depositing bHONEY'
                )
                await berpsPool.deposit_bhoney()


async def berps_pool_get_reward(account_id, key):
    berpsPool = BerpsPool(account_id, key)
    await berpsPool.get_reward_BGT()