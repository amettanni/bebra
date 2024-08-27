from modules.account import Account
from utils.config import MULTI_SWAP_ABI, BEX_POOL_CONTRACTS, BEX_POOLS, TOKEN_CONTRACTS
from settings import MainSettings as SETTINGS
import random


class Bex(Account):
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id, private_key)        
        self.bex_contract = self.get_contract(BEX_POOL_CONTRACTS['main'], MULTI_SWAP_ABI)
        

    async def swap_bera_to_coin(self, min_percent: int = 30, max_percent: int = 80, coin: str = "WBTC"):
        try:
            self.log_send(f'Swap BERA to {coin}')
            
            balance, balance_wei, decimal = await self.get_balance()

            amount, amount_wei = await self.get_percent_amount(balance, balance_wei, min_percent, max_percent)

            self.log_send(f'Swap {amount} BERA to {coin}')

            # value = self.w3.to_wei(amount, 'ether') # amount: 0.15 Bera, 1 Bera ..
            tx_data = await self.get_tx_data(amount_wei)
            steps = [
                {
                    'poolIdx': BEX_POOLS[coin]['poolIdx'],
                    'base': BEX_POOLS[coin]['base'],
                    'quote': BEX_POOLS[coin]['quote'],
                    'isBuy': BEX_POOLS[coin]['isBuy'],
                }
            ]
            
            # set to 0 for now
            # for the future adjust for the correct slippage
            # to adjust it we need to know a rate between 2 coins
            min_out = 0
            
            tx = await self.bex_contract.functions.multiSwap(steps, amount_wei, min_out).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
            
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        