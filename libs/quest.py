from bin.var import current, boss_list
from bin.buttons_generators import main_buttons
from libs.chat import Chat
from telegram.error import BadRequest
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from uuid import uuid4


class Quest:
    """
    Класс квеста с боссом
    Args:
        q_id: Индетефиктор квеста
        players: Список игроков-участников квеста
        boss_index: Номер босса
    """

    def __init__(self, q_id: str, players: dict, boss_index: int):
        self.players = {} if not players else players
        self.qn = boss_index
        self.qid = q_id

    def update(self) -> int:
        """
        Метод обновления квеста в списке
        """
        current.update({self.qid: self})
        return 100

    @staticmethod
    def create(update: Update, context: CallbackContext) -> None:
        """
        Метод создания квеста. После создания добавляет его в список активных с пустым списком игроков.
        :param context: объект бота
        :param update: объект обновления, полученного от телеграма
        """
        bot = context.bot
        mes = update.message
        chat = mes.chat
        qid = uuid4().hex[:4]
        pin = Chat.get(mes.chat_id).settings['pin']

        text = f"<code>{qid}</code>\n" \
               f"<b>🌟Элитный: {boss_list[1]}</b>\n\n" \
               f"<b>Состав:</b>\n"

        sent = chat.send_message(text=text,
                                 reply_markup=InlineKeyboardMarkup(main_buttons),
                                 parse_mode="HTML").message_id

        if pin == 'enabled':
            try:
                bot.pin_chat_message(chat_id=chat.id,
                                     message_id=sent,
                                     disable_notification=True)
            except BadRequest:
                pass

        try:
            mes.delete()
        except BadRequest:
            pass

        quest = Quest(qid, {}, 1)
        quest.update()

    @staticmethod
    def close(update: Update, context: CallbackContext) -> None:
        """
        Метод удаления взаимодействия с квестом. Удаляет квест из списка активных, что делает его недоступным.
        :param context: объект бота
        :param update: объект обновления, полученного от телеграма
        """
        mes = update.message
        quest_mes = mes.reply_to_message
        bot = context.bot

        try:
            mes.reply_to_message.edit_reply_markup(reply_markup=None)
        except (AttributeError, BadRequest):
            return

        try:
            current.pop(quest_mes.text[:4])
        except (KeyError, AttributeError):
            return

        try:
            mes.delete()
        except BadRequest:
            return

        try:
            bot.unpin_chat_message(chat_id=mes.chat_id)
        except BadRequest:
            return
