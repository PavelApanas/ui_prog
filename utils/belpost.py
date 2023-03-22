from requests import Session

def get_response(params: str):
        with Session() as session:
        response =