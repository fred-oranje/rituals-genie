"""Sample API Client."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout

TIMEOUT = 10
API_URL = "https://rituals.sense-company.com"

_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class RitualsGenieApiClient:
    def __init__(
        self, hub_hash: str, session: aiohttp.ClientSession
    ) -> None:
        """Rituals API Client."""
        self._hub_hash = hub_hash
        self._session = session

        _LOGGER.info("Set up with hash: %s", self._hub_hash)

    async def async_get_hubs(self, username: str, password: str) -> dict:
        """Login using the API"""
        url = API_URL + "/ocapi/login"
        response = await self.api_wrapper("post", url, data={"email": username, "password": password}, headers=HEADERS)

        _LOGGER.info("Login response: %s", response)

        if (response["account_hash"] == None):
            _LOGGER.info("Authentication failed: %s", response)
            raise Exception("Authentication failed")
        else:
            _LOGGER.info("Authentication success: %s", response)
            _account_hash = response["account_hash"]

        """Retrieve hubs"""
        url = API_URL + "/api/account/hubs/" + _account_hash
        response = await self.api_wrapper("get", url)

        _LOGGER.info("retrieve hubs: %s", response)

        for hub in response:
            return hub

        raise Exception("No hubs found")

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return await self.api_wrapper("get", url)

    async def async_set_title(self, value: str) -> None:
        """Get data from the API."""
        url = "https://jsonplaceholder.typicode.com/posts/1"
        await self.api_wrapper("patch", url, data={"title": value}, headers=HEADERS)

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT, loop=asyncio.get_event_loop()):
                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response.json()

                elif method == "post":
                    response = await self._session.post(url, headers=headers, json=data)
                    return await response.json()

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
