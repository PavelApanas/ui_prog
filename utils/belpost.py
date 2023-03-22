from datetime import datetime

from requests import Session

def dump_to_csv(data: dict):
        with open(f'{datetime.now().timestamp()}'.split('.')[0] + '.csv', 'w', encoding='UTF-8') as file:
            file.write('address;phone\n')
            for obj in data['data']:
                file.write(f'{obj["address"]};{obj["phone"]}\n')


def get_response(params: str):
        with Session() as session:
            response = session.get(
                url = f'https://api.belpost.by/api/v1/ops?order_by=distance{params}&display_type=list'
            )
            dump_to_csv(response.json())
