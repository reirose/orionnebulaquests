from bin.var import button, emojis

# Мэйн кнопки
main_buttons = [[button("⚔️ Готов!", callback_data='join')],
                [button("🏃 В пути!", callback_data='moving')],
                [button('❌ Выйти', callback_data='quit'),
                 button('📣 Пингануть', callback_data='ping')],
                [button("🌟 Выбор босса", callback_data='boss')]]

# Кнопки выбора босса
boss_buttons = [[button("🌟 Горгона", callback_data="boss_1"),
                 button("🌟 Гидра", callback_data='boss_2')],
                [button("🌟 Минотавр", callback_data='boss_3'),
                 button("🌟 Пирагмон", callback_data='boss_4')],
                [button("🌟 Цербер", callback_data='boss_5'),
                 button("🌟 Тифон", callback_data='boss_6')],
                [button("🌟 Дух Синдара", callback_data='boss_7'),
                 button("🌟 Немезида", callback_data='boss_8')],
                [button("🌟 Голем", callback_data='boss_9')]]


def generate_buttons(chat):
    buttons = [[button(f"📌 Пин — {emojis['settings'][chat.settings['pin']]}",
                       callback_data='pin_change')],
               [button("Закрыть", callback_data='settings_close')]]

    return buttons
