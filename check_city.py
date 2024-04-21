from settings.config import GEOCODER_API_KEY
import aiohttp
import json


async def get_check_city(city):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"http://geocode-maps.yandex.ru/1.x/?apikey={GEOCODER_API_KEY}&geocode={city}&format=json") as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            data = await response.text()
            with open('data/check_city.json', 'w', encoding='utf-8') as f:
                f.write(data)


async def check_city(city):
    await get_check_city(city)
    with open('data/check_city.json', 'r', encoding='utf-8') as check_city:
        data = json.load(check_city)
    found = data["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"]
    if found == "0":
        return True
    else:
        pass
