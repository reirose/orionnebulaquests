from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import Filters
from config.bot import dp, updater, job
from config.sql import conn

from libs.chat import Chat
from libs.quest import Quest
from libs.player import Player
from bin.button import button
from bin.service import uptime, get_vars, help_message
from bin.message_filters import is_dev_filter


def main():
    dp.add_handler(CommandHandler('boss', Quest.create))
    dp.add_handler(CommandHandler('close', Quest.close))
    dp.add_handler(CommandHandler('help', help_message))
    dp.add_handler(CommandHandler('settings', Chat.settings))
    dp.add_handler(CommandHandler('uptime', uptime, filters=is_dev_filter))
    dp.add_handler(CommandHandler('get_mem', Player.get_api_mem, filters=is_dev_filter))
    dp.add_handler(CommandHandler('get_vars', get_vars, filters=is_dev_filter))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.text, Chat.reg))

    job.run_repeating(Player.update_mem, 60)
    print("getting access")
    updater.start_polling()
    print("on air")
    updater.idle()
    conn.close()
    print("exiting...")


while __name__ == '__main__':
    main()
