from bin.var import current, emojis, boss_list, api_players
from bin.buttons_generators import main_buttons, boss_buttons

from telegram import InlineKeyboardMarkup
from telegram.error import BadRequest

from libs.player import Player


def edit_text(quest, callback_query):
    q = callback_query
    text = f"<code>{quest.qid}</code>\n" \
           f"<b>🌟Элитный: {boss_list[quest.qn]}</b>\n\n" \
           f"<b>Состав:</b>\n"

    for player in quest.players:
        p = quest.players[player][2]
        text += f"🏅{p.lvl} {p.classEmoji}{p.nickName} " \
                f"{emojis['status'][quest.players[player][0]]}\n"

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
    player = Player.get(q.from_user.id) if q.from_user.id not in api_players else api_players[q.from_user.id]

    if not player:
        return

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

    try:
        player_status = quest.players.get(q.from_user.id)[0]
    except (TypeError, AttributeError):
        player_status = None

    if player.nickName in qmes.text and q.data == 'join' and player_status != 'moving':
        return

    try:
        quest.players.update({q.from_user.id: ['ready' if q.data == 'join' else 'moving', q.from_user, player]})
    except AttributeError:
        q.answer('Набор закрыт!', show_alert=True)
        return

    api_players.update({q.from_user.id: player})
    edit_text(quest, q)
    q.answer("Скоро начнём, будьте начеку!")


def remove_player(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

    if q.from_user.id not in quest.players:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    if quest.players[q.from_user.id][2].nickName not in qmes.text:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    quest.players.pop(q.from_user.id)

    edit_text(quest, q)
    q.answer("До скорых встреч!")


def ping(update):
    q = update.callback_query
    qmes = q.message
    quest = current.get(qmes.text[:4])

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

    if q.from_user.id not in quest.players:
        q.answer("Вы не участвуете!", show_alert=True)
        return

    if quest.players[q.from_user.id][2].nickName not in qmes.text:
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

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

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

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

    quest.qn = int(q.data[-1])
    quest.update()

    edit_text(quest, q)


def close(update, bot):
    q = update.callback_query
    qmes = q.message

    if qmes.text[:4] not in current:
        q.answer("Набор закрыт!", show_alert=True)
        return

    try:
        qmes.edit_text(text=qmes.text+"\n\n<b>Набор закрыт!</b>",
                       reply_markup=None,
                       parse_mode="HTML")
    except (AttributeError, BadRequest):
        return

    try:
        current.pop(qmes.text[:4])
    except (KeyError, AttributeError):
        return

    try:
        bot.unpin_chat_message(chat_id=q.message.chat.id)
    except BadRequest:
        return
