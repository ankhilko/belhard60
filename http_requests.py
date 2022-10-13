from requests import Session
from pprint import pprint

# url1 = 'https://catalog.onliner.by/sdapi/catalog.api/search/player?player_type[0]=hifiplayer&player_type[operation]=union&group=1'
url1 = 'https://catalog.onliner.by/sdapi/catalog.api/search/player'

# TCP - Transport Protocol - повторно отправляет, пока не получено подтверждение о получении пакетов
# UDP - Transport Protocol - повторно не отправляет, не ждет подтверждения о получении пакетов

# http порт 80
# https порт 443

with Session() as session:
    response = session.get(
        url=url1,
        params={
            'player_type[0]': 'hifiplayer',
            'player_type[operation]': 'union',
            'group': 1,
        }
    )
    pprint(response.status_code)
    pprint(response.cookies)
    pprint(response.headers)
    pprint(response.text)
#    pprint(response.json())

# post -> для обратотки
# put -> для создания/полной замены/полного обновления ресурса - идемпотентный - идемпотентная функия = чистая
# patch -> для частичного обновеления/замены
# delete -> для удаления




