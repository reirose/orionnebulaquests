from bin.quest_button import join_and_ready, remove_player, ping, change_boss, choose_boss, close
from bin.chat_settings_button import change_pin, close_settings

from telegram import Update
from telegram.ext import CallbackContext


def button(update: Update, context: CallbackContext):
    q = update.callback_query
    bot = context.bot

    if q.data in ('join', 'moving'):
        join_and_ready(update)
        return

    if q.data == 'quit':
        remove_player(update)
        return

    if q.data == 'ping':
        ping(update)
        return

    if q.data == 'boss':
        change_boss(update)
        return

    if 'boss_' in q.data:
        choose_boss(update)
        return

    if q.from_user.id in [user.user.id for user in bot.get_chat_administrators(q.message.chat_id)]:
        if q.data == 'pin_change':
            change_pin(update)
            return

        if q.data == 'settings_close':
            close_settings(update)
            return

        if q.data == 'close':
            close(update, context.bot)
