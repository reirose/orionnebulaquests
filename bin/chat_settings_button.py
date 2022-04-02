from libs.chat import Chat
from bin.buttons_generators import generate_buttons


from telegram import InlineKeyboardMarkup


def change_pin(update):
    q = update.callback_query
    q.answer("")
    chat = Chat.get(q.message.chat.id)
    old = chat.settings.get('pin')
    new = "enabled" if old == 'disabled' else 'disabled'

    chat.settings.update({"pin": new})
    chat.update()

    q.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(generate_buttons(chat)))


def close_settings(update):
    q = update.callback_query
    q.message.edit_text(text="<b>Закрыто!</b>",
                        parse_mode='HTML')
