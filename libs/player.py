from config.api import api


class Player:
    def __init__(self, stats: dict):
        self.lvl = stats["level"]
        self.atk = stats["damage"]
        self.defence = stats["defence"]
        self.nickName = stats["nickName"]
        self.currentEnergy = stats["currentEnergy"]
        self.classEmoji = stats["className"][0]

    @staticmethod
    def get(player: int):

        raw = api.get_players(player)[0]
        resp = {"level": raw["level"],
                "damage": raw["damage"],
                "defence": raw["defence"],
                "nickName": raw["nickName"],
                "currentEnergy": raw["currentEnergy"],
                "className": raw["className"]}

        return resp


print(Player.get(116028074))
