from bin.var import start_time

from datetime import datetime


def uptime(bot, update):
    mes = update.message
    bot.get_me()

    upt = datetime.now() - start_time

    uptime_string = f"🔄 Время с последнего запуска: <b>{upt}</b>"
    mes.reply_text(text=uptime_string,
                   parse_mode="HTML")
