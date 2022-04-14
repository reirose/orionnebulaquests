import requests
import hashlib
from http import HTTPStatus
from json import loads
from requests.structures import CaseInsensitiveDict


class API:
    def __init__(self):
        self.token = hashlib.sha256(b'Rei:352318827:NebulaBossBot').hexdigest().upper()
        self.url = "http://llab.orion-nebula.space:1414/swiftapi/getPlayersData?"
        self.headers = CaseInsensitiveDict()
        self.headers["Authorization"] = f"Bearer {self.token}"

    def get_player(self, *args):
        for player in args:
            self.url += f"userIds={player}&"

        response = requests.get(self.url[:-1], headers=self.headers)

        print(f"[API] {str(HTTPStatus(response.status_code).description)} @ {' '.join(str(x) for x in args)}")

        if response.status_code != 200:
            return False

        players = loads(response.content.decode('utf-8'))["players"]
        self.url = "http://llab.orion-nebula.space:1414/swiftapi/getPlayersData?"

        return players


api = API()
