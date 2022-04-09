from bin.var import start_time, api_players, current, chats

from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext


def uptime(update: Update, context: CallbackContext):
    mes = update.message
    context.bot.get_me()

    upt = datetime.now() - start_time

    uptime_string = f"🔄 Время с последнего запуска: <b>{upt}</b>"
    mes.reply_text(text=uptime_string,
                   parse_mode="HTML")


def get_vars(update: Update, context: CallbackContext):
    mes = update.message
    context.bot.get_me()

    text = f"api_mem:\n{api_players}\n" \
           f"current\n{current}\n" \
           f"chats\n{chats}"

    mes.reply_text(text)
