import re

from telegram.ext import BaseFilter
from bin.var import current, superuser_id


class AddPlayerFilter(BaseFilter):
    @classmethod
    def filter(cls, message):
        return message.text == '+' and str(message.reply_to_message.message_id + message.chat_id) in current


class RemovePlayerFilter(BaseFilter):
    @classmethod
    def filter(cls, message):
        return message.text == '-' and str(message.reply_to_message.message_id + message.chat_id) in current


class PlayerIsReadyFilter(BaseFilter):
    @classmethod
    def filter(cls, message):
        return message.text == '++' and str(message.reply_to_message.message_id + message.chat_id) in current


class IsDev(BaseFilter):
    @classmethod
    def filter(cls, message):
        return message.from_user.id in superuser_id


is_dev_filter = IsDev()
add_player_filter = AddPlayerFilter()
remove_player_filter = RemovePlayerFilter()
player_is_ready_filter = PlayerIsReadyFilter()
