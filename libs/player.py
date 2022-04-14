from config.api import api
from bin.var import api_players

from json import dumps as d


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

        raw = api.get_player(player)

        if not raw:
            return False
        else:
            raw = raw[0]

        resp = {"level": raw["level"],
                "damage": raw["damage"],
                "defence": raw["defence"],
                "nickName": raw["nickName"],
                "currentEnergy": raw["currentEnergy"],
                "className": raw["className"]}

        return Player(resp)

    @staticmethod
    def update_mem(context):
        context.bot.get_me()
        id_list = list(api_players.keys())

        for tid in id_list:
            api_players.update({tid: Player.get(tid)})

    @staticmethod
    def get_api_mem(update, context):
        mes = update.message
        context.bot.get_me()

        mes.reply_text(d(api_players, indent=4))
