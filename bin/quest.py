from bin.var import current, main_buttons_markup, boss_list
from telegram.error import BadRequest
from telegram import InlineKeyboardMarkup

from uuid import uuid4


class Quest:

    def __init__(self, q_id: str, players: dict, quest_name: int):
        self.players = {} if not players else players
        self.qn = quest_name
        self.qid = q_id

    def update(self):
        current.update({self.qid: self})

    @staticmethod
    def create(bot, update):
        mes = update.message
        chat = mes.chat
        qid = uuid4().hex[:4]

        text = f"<code>{qid}</code>\n" \
               f"{boss_list[1]}\n\n" \
               f"Состав:\n"

        chat.send_message(text=text,
                          reply_markup=InlineKeyboardMarkup(main_buttons_markup),
                          parse_mode="HTML")

        try:
            bot.delete_message(message_id=mes.message_id,
                               chat_id=mes.chat_id)
        except BadRequest:
            pass

        quest = Quest(str(qid), {}, 1)
        print(qid)
        print(quest.players)
        quest.update()

    @staticmethod
    def close(bot, update):
        mes = update.message
        bot_mes = mes.reply_to_message

        current.pop(bot_mes.text[:4])
        try:
            bot.delete_message(message_id=mes.message_id,
                               chat_id=mes.chat_id)
        except BadRequest:
            pass
