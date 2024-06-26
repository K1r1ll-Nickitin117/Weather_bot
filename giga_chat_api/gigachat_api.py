from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from settings.config import AUTHORIATION_DATA


def giga_chat_weather(weather_info):
    chat = GigaChat(credentials=f'{AUTHORIATION_DATA}', verify_ssl_certs=False)

    messages = [
        SystemMessage(
            content="Ты эмпатичный бот советник выбора одежды"
        )
    ]

    user_input = f'''{weather_info}
    По этим данным помоги мне с выбором одежды'''
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)

    return res.content
