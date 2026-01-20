import requests

class RequestHelper:

    def get(url: str):

        response = requests.get(url)
        response.raise_for_status()
        return response
