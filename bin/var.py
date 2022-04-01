from telegram import InlineKeyboardButton

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

chats = {}
