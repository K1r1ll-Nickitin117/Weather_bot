from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from settings.config import AUTHORIATION_DATA
import requests
import json
from pprint import pprint


def giga_chat_weather(weather_info):
    chat = GigaChat(credentials=f'{AUTHORIATION_DATA}', verify_ssl_certs=False)

    messages = [
        SystemMessage(
            content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
        )
    ]

    user_input = f'''{weather_info}
    По этим данным помоги мне с выбором одежды'''
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)

    return res.content
