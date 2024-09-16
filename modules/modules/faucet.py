import asyncio
from modules.account import Account
from settings import MainSettings
from utils.interfaces import SoftwareException, RequestClient
from utils.utils import async_sleep
import json
from datetime import datetime, timedelta

class Faucet(RequestClient):
    def __init__(self, account: Account):
        self.account = account


    def check_faucet_allowance(self) -> bool:
        with open('faucet_allowance.json', 'r') as file:
            faucet_allowance = json.load(file)
            if self.account.address in faucet_allowance:
                faucet_last_time_used_str = faucet_allowance[self.account.address]
                faucet_last_time_used = datetime.fromisoformat(faucet_last_time_used_str)
                current_time = datetime.now()
                time_difference = current_time - faucet_last_time_used
                if time_difference > timedelta(hours=8):
                    return True
                else:
                    return False
        return True
        
    def update_faucet_usage_time(self) -> None:
        with open('faucet_allowance.json', 'r') as file:
            faucet_allowance = json.load(file)

        faucet_allowance[self.account.address] = datetime.now().isoformat()
        with open('faucet_allowance.json', 'w') as file:
            json.dump(faucet_allowance, file, indent=4)


    async def create_task_for_captcha(self):
        url = 'https://api.2captcha.com/createTask'

        proxy_tuple = self.account.proxy.split('@')

        proxy_login, proxy_password = proxy_tuple[0].split(':')
        proxy_address, proxy_port = proxy_tuple[1].split(':')

        payload = {
            "clientKey": MainSettings.TWO_CAPTCHA_API_KEY,
            "task": {
                "type": "TurnstileTask",
                "websiteURL": "https://bartio.faucet.berachain.com/",
                "websiteKey": "0x4AAAAAAARdAuciFArKhVwt",
                "userAgent": self.account.session.headers['User-Agent'],
                "proxyType": "http",
                "proxyAddress": proxy_address,
                "proxyPort": proxy_port,
                "proxyLogin": proxy_login,
                "proxyPassword": proxy_password
            }
        }

        response = await self.make_request(method="POST", url=url, json=payload)

        if not response['errorId']:
            return response['taskId']
        raise SoftwareException('Bad request to 2Captcha(Create Task)')

    async def get_captcha_key(self, task_id):
        url = 'https://api.2captcha.com/getTaskResult'

        payload = {
            "clientKey": MainSettings.TWO_CAPTCHA_API_KEY,
            "taskId": task_id
        }

        total_time = 0
        timeout = 360
        while True:
            response = await self.make_request(method="POST", url=url, json=payload)

            if response['status'] == 'ready':
                return response['solution']['token']

            total_time += 5
            await asyncio.sleep(5)

            if total_time > timeout:
                raise SoftwareException('Can`t get captcha solve in 360 second')

    async def claim_berachain_tokens(self):

        self.account.log_send(f'Claiming $BERA on faucet')

        url = 'https://bartio-faucet.berachain-devnet.com/api/claim'

        try:
            task_id = await self.create_task_for_captcha()
            captcha_key = await self.get_captcha_key(task_id)
        except Exception as e:
            self.account.log_send(f"Can't create and solve captch. {e}", status='error')
            return False

        headers = {
            "Accept": "*/*",
            "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Authorization": f"Bearer {captcha_key}",
            "Content-Type": "text/plain;charset=UTF-8",
            "Priority": "u=1, i",
            "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"128\", \"Chromium\";v=\"128\", \"Not.A/Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Referrer": "https://bartio.faucet.berachain.com/",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "body": f"{{\"address\":\"{self.account.address}\"}}",
            "method": "POST",
            "mode": "cors",
            "Dnt": "1",
            "Origin": "https://bartio.faucet.berachain.com"
        }

        params = {
            "address": f"{self.account.address}"
        }

        try:
            await self.make_request(method="POST", url=url, params=params, json=params, headers=headers)
            self.account.log_send(f'$BERA was successfully claimed on faucet', status='success')

            await self.account.session.close()
            self.update_faucet_usage_time()
        except Exception as e:
            self.account.log_send(f"Error happend while claiming $BERA from faucet. {e}", status='error')
            return False
        
        await async_sleep(
            MainSettings.FAUCET_SLEEP[0], MainSettings.FAUCET_SLEEP[1],
            True, self.account.account_id, self.account.private_key, 'after claiming test $BERA'
        )

        return True
