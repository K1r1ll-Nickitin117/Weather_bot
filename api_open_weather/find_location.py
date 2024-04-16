import aiohttp
import asyncio
import json
from config import OPEN_WEATHER_API_KEY


# class
async def get_weather(lat, lon):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            data = await response.text()
            with open('data/weather.json', 'w', encoding='utf-8') as f:
                f.write(data)


async def find_location(location):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPEN_WEATHER_API_KEY}') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            data = await response.text()
            with open('data/find_location.json', 'w', encoding='utf-8') as f:
                f.write(data)

    with open('data/find_location.json', 'r', encoding='utf-8') as cooords:
        coords_data = json.load(cooords)
    lat = coords_data[0]['lat']
    lon = coords_data[0]['lon']
    await get_weather(lat, lon)
