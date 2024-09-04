import asyncio
import aiohttp.client_exceptions
from abc import ABC


class PriceImpactException(Exception):
    pass


class BlockchainException(Exception):
    pass


class SoftwareException(Exception):
    pass


class SoftwareExceptionWithoutRetry(Exception):
    pass


class WrongGalxeCode(Exception):
    pass


class RequestClient(ABC):
    def __init__(self, account):
        self.account = account

    async def make_request(self, method:str = 'GET', url:str = None, headers:dict = None, params: dict = None,
                           data:str = None, json:dict = None, module_name:str = 'Request'):

        errors = None

        total_time = 0
        timeout = 360
        while True:
            try:
                async with self.account.session.request(
                        method=method, url=url, headers=headers, data=data, params=params, json=json
                ) as response:
                    if response.status in [200, 201]:
                        data = await response.json()
                        if isinstance(data, dict):
                            errors = data.get('errors')
                        elif isinstance(data, list) and isinstance(data[0], dict):
                            errors = data[0].get('errors')

                        if not errors:
                            return data
                        elif 'have been marked as inactive' in f"{errors}":
                            raise SoftwareExceptionWithoutRetry(
                                f"Bad request to {self.__class__.__name__}({module_name}) API: {errors[0]['message']}")
                        else:
                            raise SoftwareException(
                                f"Bad request to {self.__class__.__name__}({module_name}) API: {errors[0]['message']}")

                    raise SoftwareException(
                        f"Bad request to {self.__class__.__name__}({module_name}) API: {await response.text()}")
            except aiohttp.client_exceptions.ServerDisconnectedError as error:
                total_time += 15
                await asyncio.sleep(15)
                if total_time > timeout:
                    raise SoftwareException(error)
                continue
            except SoftwareExceptionWithoutRetry as error:
                raise SoftwareExceptionWithoutRetry(error)
            except Exception as error:
                raise SoftwareException(error)
