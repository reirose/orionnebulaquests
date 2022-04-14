from bin.var import start_time, api_players, current, chats, boss_lvl

from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext


def check_compability(player, quest):
    if abs(player.lvl - boss_lvl[quest.qn]) >= 3:
        return False
    else:
        return True


def help_message(update: Update, context: CallbackContext):
    context.bot.get_me()
    response = "<b>Справка</b>\n\n" \
               "    Бот предназначен для более удобного отслеживания игроков, желающих участвовать в убийстве " \
               "<b>🌟 Элитного босса</b> в локациях <b>🌏 Мира Ориона</b>.\n" \
               "    При появлении знака ❗️ возле Вашего ника следует знать, что вы или не сможете участвовать в " \
               "рейде, или у Вас будет штраф по опыту.\n\n" \
               "<i>Примечание: бот работает с использованием API игры для получения информации об игроке. Доступ" \
               "к характеристикам Вашего игрока есть только у кода бота. Если вы сомневаетесь в соблюдении" \
               " конфиденциальности Ваших данных, пишите <a href='t.me/reirose'>мне</a>.</i>\n"
    update.message.reply_text(text=response, parse_mode='HTML')


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
