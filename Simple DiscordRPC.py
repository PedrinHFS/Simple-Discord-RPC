from pypresence import Presence
import time
import yaml
import os


client_id = ''

detalhes = {}

if (os.path.getsize('./configuracoes.yaml') == 0):
    detalhes = {
        'client_id': input('Qual é o id da sua aplicação:\n'),
        'large_image_key': input('Qual é a key da sua large image?\n'),
        'small_image_key': input('Qual é a key da sua small image?\n'),
        'large_image_text': input('Qual é o texto da sua large image?\n'),
        'small_image_text': input('Qual é o texto da sua small image?\n'),
        'details': input('Qual é o primeiro texto da sua rich presence?\n'),
        'state': input('Qual é o segundo texto da sua rich presence?\n'),
    }
    with open('./configuracoes.yaml', 'w') as f:
        yaml.dump(detalhes, f)
else:
    with open('./configuracoes.yaml') as f:
        detalhes = yaml.load(f, Loader=yaml.FullLoader)

RPC = Presence(detalhes['client_id'])
RPC.connect()

primeiro = False


def setPresence(string):
    RPC.update(large_image=detalhes['large_image_key'], start=time.time(), large_text=detalhes['large_image_text'],
               small_image=detalhes['small_image_key'], small_text=detalhes['large_image_text'],
               details=detalhes['details'], state=detalhes['state'])


while True:
    if not primeiro:
        setPresence(detalhes)
        primeiro = True
        print(
            'A rich presence foi inserida com sucesso! Caso queira atualizar ela, re-abra o programa e faça o processo novamente')
    time.sleep(60)
