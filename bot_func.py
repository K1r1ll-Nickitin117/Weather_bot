from api_open_weather.open_weather_api import OpenWeatherApi


class BotFunc(OpenWeatherApi):
    async def location_now(self):
        print(1)

    async def weather(self):
        print(2)

    async def my_location(self):
        print(3)

    async def change_location(self):
        print(4)

    async def what_to_wear(self):
        print(5)

    async def help(self):
        print(6)

    async def start_bot(self):
        print(7)

    async def restart_bot(self):
        print(8)
