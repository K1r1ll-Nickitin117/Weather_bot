# Бот для просмотра погоды
## Функционал бота:
1) Просмотр погоды в любой локации
2) Смена локации
3) Помощь с выбором одежды в зависимости от погоды
4) История поиска
## Команды бота:
1) /weather Покажет погоду сейчас
2) /help Справка по боту
3) /start старт бота
4) /restart рестарт бота
5) /stat просмотр истории поиска
## Запуск бота:
1) Создать файл config.py
```python
BOT_TOKEN = 'TOKEN'
OPEN_WEATHER_API_KEY = 'api_key'
GEOCODER_API_KEY = 'Geocoder_yandex_api_key'
AUTHORIATION_DATA = 'authoriation_data_from_gigachat_api'
```
2) Установить зависимости
```
pip install -r requirements.txt
```
