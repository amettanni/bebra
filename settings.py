class MainSettings:
    MAX_GAS = 100

    GAS_MULTIPLAYER = 1

    RANDOM_WALLETS = True

    REMOVE_WALLET = False

    USE_PROXY = True

    START_PERIOD = [1, 5]
    
    REPEATS_PER_WALLET = 1

    SLEEP_AFTER_WORK = [180, 400]

    SLEEP_INSIDE_MODULE = [30, 120]

    SLIPPAGE = 1

    GAS_LIMIT = 500000

    GAS_PRICE = 0.001250

    CUSTOM_ROUTES_MODULES = [
        ['low_swap_bera_to_random_coin', 'swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey'],
        ['swap_bera_honey', 'berps_pool_deposit'],
        ['low_swap_bera_to_random_coin', 'berps_pool_get_reward', 'bend_get_reward'],
        ['swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey', 'swap_bera_honey', 'berps_pool_deposit'],
        ['swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey'],
        ['swap_bera_honey', 'berps_pool_deposit', 'berps_pool_get_reward', 'bend_get_reward'],
        ['low_swap_bera_to_random_coin', 'swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey', 'swap_bera_honey', 'berps_pool_deposit'],
        ['berps_pool_get_reward', 'bend_get_reward'],
        ['low_swap_bera_to_random_coin', 'swap_bera_honey', 'berps_pool_deposit'],
        ['swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey', 'low_swap_bera_to_random_coin'],
        ['berps_pool_get_reward', 'bend_get_reward', 'swap_bera_honey', 'berps_pool_deposit'],
        ['low_swap_bera_to_random_coin', 'swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey'],
        ['swap_bera_honey', 'berps_pool_deposit', 'swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey'],
        ['low_swap_bera_to_random_coin', 'swap_bera_honey', 'berps_pool_deposit'],
        ['swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey', 'berps_pool_get_reward', 'bend_get_reward'],
        ['swap_bera_honey', 'berps_pool_deposit', 'low_swap_bera_to_random_coin'],
        ['swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey', 'swap_bera_honey', 'berps_pool_deposit'],
        ['low_swap_bera_to_random_coin', 'berps_pool_get_reward', 'bend_get_reward', 'swap_bera_honey', 'berps_pool_deposit'],
        ['berps_pool_get_reward', 'bend_get_reward', 'swap_bera_wbtc', 'bend_supply_wbtc_and_borrow_honey'],
        ['low_swap_bera_to_random_coin', 'swap_bera_honey', 'berps_pool_deposit']
    ]


class ModulesSettings:
    
    class Bex:
        PERCENTS = [10, 20]
        LOW_PERCENTS = [1, 5]


    class BerpsPool:
        PERCENTS = [10, 30]


    class Bend:
        PERCENTS = [20, 40]