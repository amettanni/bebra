from modules.account import Account
from utils.config import BEND_POOL_ABI, BEND_POOL_CONTRACTS, BEND_ATOKEN_ABI, REWARD_ABI
from settings import MainSettings as SETTINGS
import random


class Bend(Account):
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id, private_key)
        
        self.bend_pool_contract = self.get_contract(BEND_POOL_CONTRACTS['main'], BEND_POOL_ABI)
        self.bend_pool_reward_contract = self.get_contract(BEND_POOL_CONTRACTS['reward'], REWARD_ABI)
   
    async def approve_wbtc(self):
        try:
            self.log_send(f'Approve WBTC on Bend Pool.')

            return await self.approve(BEND_POOL_CONTRACTS['WBTC'], BEND_ATOKEN_ABI, BEND_POOL_CONTRACTS['main'])
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        

    async def supply_wbtc(
        self,
        min_percent: int = 60, 
        max_percent: int = 95,
    ):
        try:
            balance, balance_wei, decimal = await self.get_balance(BEND_POOL_CONTRACTS['WBTC'])

            amount, amount_wei = await self.get_percent_amount(balance, balance_wei, min_percent, max_percent)

            self.log_send(f'Supply {amount} WBTC to the Bend Pool')

            tx_data = await self.get_tx_data()
            
            tx = await self.bend_pool_contract.functions.supply(
                BEND_POOL_CONTRACTS['WBTC'], 
                amount_wei,
                self.address,
                decimal # decimals? 8
                ).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        
    async def approve_weth(self):
        try:
            self.log_send(f'Approve WETH on Bend Pool.')

            return await self.approve(BEND_POOL_CONTRACTS['WETH'], BEND_ATOKEN_ABI, BEND_POOL_CONTRACTS['main'])
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        

    async def supply_weth(
        self,
        min_percent: int = 60, 
        max_percent: int = 95,
    ):
        try:
            balance, balance_wei, decimal = await self.get_balance(BEND_POOL_CONTRACTS['WETH'])

            amount, amount_wei = await self.get_percent_amount(balance, balance_wei, min_percent, max_percent)

            self.log_send(f'Supply {amount} WETH to the Bend Pool')

            tx_data = await self.get_tx_data()
            
            tx = await self.bend_pool_contract.functions.supply(
                BEND_POOL_CONTRACTS['WETH'], 
                amount_wei,
                self.address,
                decimal # decimals?
                ).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        

    async def borrow_honey(self):
        try:
            
            base_amount_wei = 1000000000000000000  # 1 HONEY // amount to supply

            multiplier = random.randint(1, 20) / 4

            amount_wei = int(base_amount_wei * multiplier)

            self.log_send(f'Borrow {multiplier} HONEY from Bend Pool')

            tx_data = await self.get_tx_data()

            # idk what is it, but it's 2
            interestRateMode = 2
            refCode = 0

            borrow_data = (BEND_POOL_CONTRACTS['HONEY'], amount_wei, interestRateMode, refCode, self.address)
            tx = await self.bend_pool_contract.functions.borrow(*borrow_data).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        

    async def get_reward_BGT(self):
        try:
            self.log_send(f'Get reward (BGT tokens) from Bend Pool')

            tx_data = await self.get_tx_data()
            
            tx = await self.bend_pool_reward_contract.functions.getReward(self.address).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False