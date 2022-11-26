import telebot
from telebot import types
import time
import random

bot = telebot.TeleBot('5627151433:AAE9GbzdGGom3S1-LM88m1iSVvvVm7Q9_UI')

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️ 👍 😢


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # region Начальный уровень
    if call.data == 'next_simple1' or call.data == 'next_simple2':
        a = random.randint(1, 20)
        s = random.choice(['-', '+'])
        b = random.randint(1, 20)
        bot.send_message(call.message.chat.id, f'Решите мой пример: {a} {s} {b} = ?\n🤖 Просто отправьте мне свой ответ 👇')

        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_simple1'))

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_simple2'))

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)

            if s == '+':
                if x == (a + b):
                    bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
                else:
                    bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)
            elif s == '-':
                if x == (a - b):
                    bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
                else:
                    bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)

        bot.register_next_step_handler(call.message, message_input)
    # endregion Начальный уровень

    if call.data == 'next_middle1' or call.data == 'next_middle2':
        pass


# region Команда START
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Ваш user ID: `{message.chat.id}`', parse_mode='Markdown')

    first_name = message.from_user.first_name
    message_text = f'Привет *{first_name}*! Этот бот помогает тренировать устный счет в уме, просто выбери нужный уровень сложности 👇\n\n' \
                   f'Чтобы найти автора, воспользуйтесь [ссылкой](https://t.me/lizzerd18).'


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Начальный уровень')
    markup.add(btn1)


    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
# endregion Команда START

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    # region Начальный уровень
    if get_message_bot == "Начальный уровень":
        a = random.randint(1, 20)
        s = random.choice(['-', '+'])
        b = random.randint(1, 20)
        bot.send_message(message.chat.id, f'Решите мой пример: {a} {s} {b} = ?\n🤖 Просто отправьте мне свой ответ 👇')

        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_simple1'))

        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_simple2'))

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)

            if s == '+':
                if x == (a + b):
                    bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
                else:
                    bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)
            elif s == '-':
                if x == (a - b):
                    bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
                else:
                    bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)
        bot.register_next_step_handler(message, message_input)
    # endregion Начальный уровень

    elif get_message_bot == "Средний уровень":
        pass

    elif get_message_bot == "Сложный уровень":
        pass

    else:
        bot.send_message(message.chat.id, '🤖 я не знаю как Вам ответить на это..')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)