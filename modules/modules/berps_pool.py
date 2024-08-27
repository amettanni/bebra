from modules.account import Account
from utils.config import BERPS_POOL_CONTRACTS, BERPS_POOL_ABI, BERPS_VAULT_APPROVE_ABI, BERA_REWARDS_VAULT_ABI
from settings import MainSettings as SETTINGS


class BerpsPool(Account):
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id, private_key)
        
        self.berps_pool_contract = self.get_contract(BERPS_POOL_CONTRACTS['BHONEY'], BERPS_POOL_ABI)
        self.berachain_rewards_vault_contract = self.get_contract(BERPS_POOL_CONTRACTS['BHONEY'], BERA_REWARDS_VAULT_ABI)


    async def approve_honey(self):
        try:
            self.log_send(f'Approve HONEY on Berps Pool.')

            return await self.approve(BERPS_POOL_CONTRACTS['HONEY'], BERPS_VAULT_APPROVE_ABI)
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False


    async def deposit_honey(
        self,
        min_percent: int = 70,
        max_percent: int = 90,
    ):
        try:
            balance, balance_wei, decimal = await self.get_balance(BERPS_POOL_CONTRACTS['HONEY'])

            amount, amount_wei = await self.get_percent_amount(balance, balance_wei, min_percent, max_percent)

            self.log_send(f'Deposit {amount} HONEY on Berps Pool.')
            
            tx_data = await self.get_tx_data()
            
            tx = await self.berps_pool_contract.functions.deposit(amount_wei, self.address).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        
    async def approve_bhoney(self):
        try:
            self.log_send(f'Approve bHONEY on Berps Pool.')

            return await self.approve(BERPS_POOL_CONTRACTS['BHONEY'], BERPS_POOL_ABI)
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False


    async def deposit_bhoney(self):
        try:
            balance, balance_wei, decimal = await self.get_balance(BERPS_POOL_CONTRACTS['BHONEY'])
        
            self.log_send(f'Deposit {balance} bHONEY on Bera Rewards Vault.')

            tx_data = await self.get_tx_data()
            
            tx = await self.berachain_rewards_vault_contract.functions.stake(balance_wei).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False
        

    async def get_reward_BGT(self):
        try:
            self.log_send(f'Get reward (BGT tokens) from  Bera Rewards Vault.')

            tx_data = await self.get_tx_data()
            
            tx = await self.berachain_rewards_vault_contract.functions.getReward(self.address).build_transaction(tx_data)
            
            tx_status = await self.execute_transaction(tx)
            
            return tx_status
        
        except Exception as e:
            self.log_send(f'Error in module «{__class__.__name__}»: {e}', status='error')
            return False