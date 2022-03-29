from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
from config.bot import dp, updater
from config.sql import conn

from bin.quest import Quest
from bin.quest_button import button


def main():
    dp.add_handler(CommandHandler('boss', Quest.create))
    dp.add_handler(CommandHandler('close', Quest.close))

    # dp.add_handler(MessageHandler(add_player_filter, Quest.add_player))
    # dp.add_handler(MessageHandler(remove_player_filter, Quest.remove_player))
    # dp.add_handler(MessageHandler(player_is_ready_filter, Quest.player_is_ready))

    dp.add_handler(CallbackQueryHandler(button))

    print("getting access")
    updater.start_polling()
    print("on air")
    updater.idle()
    conn.close()


while __name__ == '__main__':
    main()
