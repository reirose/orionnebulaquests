from telegram import InlineKeyboardButton

button = InlineKeyboardButton
current = dict()

boss_list = {1: 'Горгона 🎖5',
             2: "Гидра 🎖10",
             3: "Минотавр 🎖15",
             4: "Пирагмон 🎖20",
             5: "Цербер 🎖25",
             6: "Тифон 🎖30",
             7: "Дух Синдара 🎖40",
             8: "Немезида 🎖50",
             9: "Голем"}

status = {"ready": "✅",
          "not_ready": "❌",
          'moving': "🏃"}

main_buttons_markup = [[InlineKeyboardButton("⚔️ Готов!", callback_data='join')],
                       [button("🏃 В пути!", callback_data='moving')],
                       [InlineKeyboardButton('❌ Выйти', callback_data='quit'),
                        InlineKeyboardButton('📣 Пингануть', callback_data='ping')],
                       [InlineKeyboardButton("🌟 Выбор босса", callback_data='boss')]]

boss_buttons_markup = [[button("🌟 Горгона", callback_data="boss_1"),
                        button("🌟 Гидра", callback_data='boss_2')],
                       [button("🌟 Минотавр", callback_data='boss_3'),
                        button("🌟 Пирагмон", callback_data='boss_4')],
                       [button("🌟 Цербер", callback_data='boss_5'),
                        button("🌟 Тифон", callback_data='boss_6')],
                       [button("🌟 Дух Синдара", callback_data='boss_7'),
                        button("🌟 Немезида", callback_data='boss_8')],
                       [button("🌟 Голем", callback_data='boss_9')]]
