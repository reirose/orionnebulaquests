from telegram import InlineKeyboardButton

from datetime import datetime

start_time = datetime.now()

button = InlineKeyboardButton  # Shortcut
current = dict()  # Список активных квестов
emojis = {
    'status': {"ready": "✅",
               "not_ready": "❌",
               'moving': "🏃"},
    'settings': {'enabled': '✅',
                 'disabled': '❌'}
}

boss_list = {1: 'Горгона 🎖5',
             2: "Гидра 🎖10",
             3: "Минотавр 🎖15",
             4: "Пирагмон 🎖20",
             5: "Цербер 🎖25",
             6: "Тифон 🎖30",
             7: "Дух Синдара 🎖40",
             8: "Немезида 🎖50",
             9: "Голем"}

superuser_id = [352318827]
api_players = {}

chats = {}
