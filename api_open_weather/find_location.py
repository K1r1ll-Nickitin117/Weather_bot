import aiohttp
import asyncio
import json
from config import OPEN_WEATHER_API_KEY


# class
async def find_lat_and_lon(lat, lon):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            data = await response.text()
            with open('data/find_location.json', 'w') as f:
                f.write(data)


async def find_location(location):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPEN_WEATHER_API_KEY}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            data = await response.text()
            with open('data/find_coords.json', 'w') as f:
                f.write(data)


def weather_forecast():
    pass
# asyncio.run(find_location(47.23571, 39.70151))
# asyncio.run(find_location('Ростов-на-Дону'))