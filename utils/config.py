import json


with open('data/rpc.json', 'r') as file:
    RPC = json.load(file)

with open('accounts.txt', 'r') as file:
    ACCOUNTS = [row.strip() for row in file]


with open('data/bend atoken/abi.json', "r") as file:
    BEND_ATOKEN_ABI = json.load(file)

with open('data/bend pool/abi.json', "r") as file:
    BEND_POOL_ABI = json.load(file)

with open('data/berachainRewardsVault/abi.json', "r") as file:
    BERA_REWARDS_VAULT_ABI = json.load(file)

with open('data/berps vault approve/abi.json', "r") as file:
    BERPS_VAULT_APPROVE_ABI = json.load(file)

with open('data/berps pool/abi.json', "r") as file:
    BERPS_POOL_ABI = json.load(file)

with open('data/erc20 tokens/abi.json', "r") as file:
    ERC_20_ABI = json.load(file)

with open('data/multi swap/abi.json', "r") as file:
    MULTI_SWAP_ABI = json.load(file)

with open('data/reward/abi.json', "r") as file:
    REWARD_ABI = json.load(file)



MAX_APPROVE = 2**128 - 1


BERPS_POOL_CONTRACTS = {
    'BHONEY': '0x1306D3c36eC7E38dd2c128fBe3097C2C2449af64',
    'HONEY': '0x0E4aaF1351de4c0264C5c7056Ef3777b41BD8e03',
    'main': '0xC5Cb3459723B828B3974f7E58899249C2be3B33d',
}

BEX_POOL_CONTRACTS = {
    'main': '0x21e2C0AFd058A89FCf7caf3aEA3cB84Ae977B73D',
}

BEX_POOLS = {
    'WBTC': {
        'poolIdx': 36001,
        'base': '0x2577D24a26f8FA19c1058a8b0106E2c7303454a4',
        'quote': '0x0000000000000000000000000000000000000000',
        'isBuy': False
    },
    "HONEY": {
        'poolIdx': 36000,
        'base': '0x0E4aaF1351de4c0264C5c7056Ef3777b41BD8e03',
        'quote': '0x0000000000000000000000000000000000000000',
        'isBuy': False,
    },
    "USDC": {
        'poolIdx': 36000,
        'base': '0x0000000000000000000000000000000000000000',
        'quote': '0xd6D83aF58a19Cd14eF3CF6fe848C9A4d21e5727c',
        'isBuy': True,
    },
    "USDT": {
        'poolIdx': 36000,
        'base': '0x05D0dD5135E3eF3aDE32a9eF9Cb06e8D37A6795D',
        'quote': '0x0000000000000000000000000000000000000000',
        'isBuy': False,
    },
    "WETH": {
        'poolIdx': 36001,
        'base': '0x0000000000000000000000000000000000000000',
        'quote': '0xE28AfD8c634946833e89ee3F122C06d7C537E8A8',
        'isBuy': True,
    },
    "DAI": {
        'poolIdx': 36002,
        'base': '0x0000000000000000000000000000000000000000',
        'quote': '0x806Ef538b228844c73E8E692ADCFa8Eb2fCF729c',
        'isBuy': True,
    },
}

BEND_POOL_CONTRACTS = {
    'main': "0x30A3039675E5b5cbEA49d9a5eacbc11f9199B86D",
    'WBTC': "0x2577D24a26f8FA19c1058a8b0106E2c7303454a4",
    "HONEY": "0x0E4aaF1351de4c0264C5c7056Ef3777b41BD8e03",
    "WETH": "0xE28AfD8c634946833e89ee3F122C06d7C537E8A8",
    'reward': '0x2E8410239bB4b099EE2d5683e3EF9d6f04E321CC'
}

TOKEN_CONTRACTS = {
    'WBTC': "0x2577D24a26f8FA19c1058a8b0106E2c7303454a4",
    "HONEY": "0x0E4aaF1351de4c0264C5c7056Ef3777b41BD8e03",
    "BGT": "0xbDa130737BDd9618301681329bF2e46A016ff9Ad",
    "USDC": "0xd6D83aF58a19Cd14eF3CF6fe848C9A4d21e5727c",
    "WETH": "0xE28AfD8c634946833e89ee3F122C06d7C537E8A8",
    "BERA": "0x7507c1dc16935B82698e4C63f2746A2fCf994dF8",
    "USDT": "0x05D0dD5135E3eF3aDE32a9eF9Cb06e8D37A6795D",
    "DAI": "0x806Ef538b228844c73E8E692ADCFa8Eb2fCF729c",
}