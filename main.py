import asyncio
from loguru import logger
import sys
# import questionary

from utils.launch import start_tasks
from utils.utils import get_wallets
from utils.modules import *


# submenus = {
#     'start-menu': [
#         questionary.Choice('🚀 Custom Module Routes', 'custom-routes'),
#         questionary.Choice('✨ One Selected Module', 'one_selected_module'),
#         # questionary.Choice('📥 OKX Balance Modules', 'okx_modules'),
#         # questionary.Choice('💼 Base Balance Checker', 'balance-checker'),
#         questionary.Choice('❌ Exit', 'exit'),
#     ],
#     'one_selected_module': [
#         # questionary.Choice('● Swap on 1inch', swap_inch),
#         questionary.Choice('● Swap from Bera to WBTC', swap_bera_wbtc),
#         questionary.Choice('● Low Swap from Bera to Coin', low_swap_bera_to_random_coin),
#         questionary.Choice('● Bend Supply WBTC and Borrow HONEY', bend_supply_wbtc_and_borrow_honey ),
#         questionary.Choice('● Bend Supply WETH and Borrow HONEY', bend_supply_weth_and_borrow_honey ),
#         questionary.Choice('● Bend Get Reward', bend_get_reward),
#         questionary.Choice('● Berps Pool Deposit', berps_pool_deposit),
#         questionary.Choice('● Berps Pool Get Reward', berps_pool_get_reward),
#     ],
# }

# def show_submenu(selected_mode):
#     submenu = submenus[selected_mode]
#     module = questionary.select(
#         message='Choose the desired module.',
#         choices=submenu,
#         qmark='📌 ',
#         pointer='➡️ '
#     ).ask()

#     return module

def main():

    # account_number_to_start_from = input('Enter number of the account to start from (Leave empty for default) :       ')
    # if account_number_to_start_from != '':
    #     account_number_to_start_from = int(account_number_to_start_from)
    #     data = get_wallets(account_number_to_start_from)
    # else:
    #     data = get_wallets()

    data = get_wallets()

    # selected_mode = questionary.select(
    #     message='Select a mode to start the software.',
    #     choices=submenus['start-menu'],
    #     qmark='📌 ',
    #     pointer='➡️ '
    # ).ask()
    
    # if selected_mode in submenus:
    #     selected_mode = show_submenu(selected_mode)
    #     asyncio.run(start_tasks(data, selected_mode))
    # # elif selected_mode == 'balance-checker': asyncio.run(run_check_balance(data))
    # elif selected_mode == 'exit': sys.exit()
    # else: asyncio.run(start_tasks(data, None))

    asyncio.run(start_tasks(data, None))

if __name__ == '__main__':
    logger.add('logs.log')
    main()