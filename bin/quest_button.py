from bin.var import current, emojis, boss_list
from bin.buttons_geenrators import main_buttons, boss_buttons

from telegram import InlineKeyboardMarkup
from telegram.error import BadRequest


def edit_text(quest, callback_query):
    q = callback_query
    text = f"<code>{quest.qid}</code>\n" \
           f"<b>🌟Элитный: {boss_list[quest.qn]}</b>\n\n" \
           f"<b>Состав:</b>\n"

    for player in quest.players:
        text += f"{emojis['status'][quest.players[player][0]]} {quest.players[player][1].first_name}\n"

    try:
        q.edit_message_text(text=text,
                            reply_markup=InlineKeyboardMarkup(main_buttons),
                            parse_mode="HTML")
    except BadRequest:
        pass


def join_and_ready(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    try:
        player_status = quest.players.get(q.from_user.id)[0]
    except TypeError or AttributeError:
        player_status = None

    if q.from_user.first_name in qmes.text and q.data == 'join' and player_status != 'moving':
        return

    try:
        quest.players.update({q.from_user.id: ['ready' if q.data == 'join' else 'moving', q.from_user]})
    except AttributeError:
        q.answer('Набор закрыт!', show_alert=True)
        return

    edit_text(quest, q)
    q.answer("Скоро начнём, будьте начеку!")


def remove_player(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    if q.from_user.first_name not in qmes.text:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    quest.players.pop(q.from_user.id)

    edit_text(quest, q)
    q.answer("До скорых встреч!")


def ping(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    if q.from_user.first_name not in qmes.text:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    try:
        players = list(quest.players.keys())
    except AttributeError:
        q.answer('Набор закрыт!', show_alert=True)
        return

    while players:
        text = "<b>Начинаем квест!</b>\n"
        for i in range(0, 4):
            try:
                text += f"@{quest.players[players[0]][1].username}\n"
            except IndexError:
                break
            players.pop(0)

        qmes.reply_text(text=text,
                        parse_mode="HTML")


def change_boss(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    if q.from_user.id not in quest.players:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    q.edit_message_text(text=f"<code>{quest.qid}</code>\nВыберите босса:",
                        reply_markup=InlineKeyboardMarkup(boss_buttons),
                        parse_mode="HTML")
    q.answer('')


def choose_boss(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    quest.qn = int(q.data[-1])
    quest.update()

    edit_text(quest, q)
