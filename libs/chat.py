from config.sql import cur, query
from bin.var import chats
from bin.buttons_geenrators import generate_buttons

from json import dumps
from telegram import InlineKeyboardMarkup


class Chat:

    def __init__(self, chat_id: int, settings: dict):
        self.chat_id = chat_id
        self.settings = settings
        self.pin_settings = settings.get('pin')

    @staticmethod
    def update_list():
        query("""SELECT * FROM chats""")
        result = cur.fetchall()

        if not result:
            return

        for chat in result:
            chats.update({chat[0]: chat[1]})

        return

    @staticmethod
    def get(chat_id):
        query("""SELECT * FROM chats WHERE chat_id = %i""" % chat_id)

        try:
            return Chat(chat_id, cur.fetchall()[0][1])
        except TypeError:
            return 404

    def update(self):
        query("""UPDATE chats SET setiings = '%s' WHERE chat_id = %i""" % (dumps(self.settings,
                                                                                 ensure_ascii=False),
                                                                           self.chat_id))
        return

    @staticmethod
    def reg(bot, update):
        bot.get_me()
        if update.message.chat_id in chats:
            return

        query("""INSERT INTO chats (chat_id, setiings) VALUES (%i, '%s')""" % (update.message.chat_id,
                                                                               dumps({"pin": 'disabled'})))
        Chat.update_list()
        return

    @staticmethod
    def settings(bot, update):
        mes = update.message
        chat = Chat.get(mes.chat_id)

        if mes.from_user.id not in [user.user.id for user in bot.get_chat_administrators(mes.chat_id)]:
            mes.reply_text('Настройки доступны только для администраторов чата!')
            return

        if chat == 404:
            print(chat)
            return

        text = f"Чат <code>{chat.chat_id}</code> — настройки"
        settings_buttons = generate_buttons(chat)

        bot.send_message(chat_id=mes.chat_id,
                         text=text,
                         parse_mode='HTML',
                         reply_markup=InlineKeyboardMarkup(settings_buttons))
