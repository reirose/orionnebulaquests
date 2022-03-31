from libs.chat import Chat
from bin.var import button, emojis

from telegram import InlineKeyboardMarkup


def generate_buttons(chat: Chat):
    buttons = [[button(f"📌 Пин — {emojis['settings'][chat.settings['pin']]}",
                       callback_data='pin_change')]]

    return buttons


def change_pin(update):
    q = update.callback_query
    q.answer("")
    chat = Chat.get(q.message.chat.id)
    old = chat.settings.get('pin')
    new = "enabled" if old == 'disabled' else 'disabled'

    chat.settings.update({"pin": new})
    chat.update()

    q.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(generate_buttons(chat)))
