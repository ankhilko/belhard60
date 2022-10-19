from aiohttp import ClientSession

# url1 = 'https://catalog.onliner.by/sdapi/catalog.api/search/player?player_type[0]=hifiplayer&player_type[operation]=union&group=1'

async def get_responce():
        async with ClientSession(base_url='https://catalog.onliner.by') as session:
            response = await session.get(
                url='/sdapi/catalog.api/search/player',
                params= {
                    'player_type[0]': 'hifiplayer',
                    'player_type[operation]': 'union',
                    'group': '1'}
            )

        print(response.status)
        print(response.headers)
        print(response.cookies)
        print(await response.text())
        print(await response.json())

import asyncio

async def main():
    task = [asyncio.create_task(get_responce()) for i in range(10)]
    await asyncio.wait(task)

asyncio.run(main())
