from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import Filters
from config.bot import dp, updater
from config.sql import conn

from libs.chat import Chat
from libs.quest import Quest
from bin.button import button
from bin.service import uptime
from bin.message_filters import is_dev_filter


def main():
    dp.add_handler(CommandHandler('boss', Quest.create))
    dp.add_handler(CommandHandler('close', Quest.close))
    dp.add_handler(CommandHandler('settings', Chat.settings))
    dp.add_handler(CommandHandler('uptime', uptime, filters=is_dev_filter))

    # dp.add_handler(MessageHandler(add_player_filter, Quest.add_player))
    # dp.add_handler(MessageHandler(remove_player_filter, Quest.remove_player))
    # dp.add_handler(MessageHandler(player_is_ready_filter, Quest.player_is_ready))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(MessageHandler(Filters.text, Chat.reg))

    print("getting access")
    updater.start_polling()
    print("on air")
    updater.idle()
    conn.close()
    print("exiting...")


while __name__ == '__main__':
    main()
