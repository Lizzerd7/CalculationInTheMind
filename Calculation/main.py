import telebot
from telebot import types
import time
import random

bot = telebot.TeleBot('5627151433:AAE9GbzdGGom3S1-LM88m1iSVvvVm7Q9_UI') #IP токен бота

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️ 👍 😢


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == 'next_simple1' or call.data == 'next_simple2':
        a = random.randint(1, 30)
        s = ('+')
        b = random.randint(1, 30)
        bot.send_message(call.message.chat.id, f'Решите мой пример: {a} {s} {b} = ?\n🤖 Просто отправьте мне свой ответ 👇')#бот отправляет сообщение

        markup1 = types.InlineKeyboardMarkup(row_width=1)#кнопка в сообщение
        markup1.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_simple1'))#текст на кнопке в сообщение

        markup2 = types.InlineKeyboardMarkup()#кнопка в сообщение
        markup2.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_simple2'))#текст на кнопке в сообщение

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)#x=текст с клавиатуры
            if x == (a + b):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)

        bot.register_next_step_handler(call.message, message_input)

    if call.data == 'next_middle1' or call.data == 'next_middle2':
        o = random.randint(1, 100)
        s = ('+')
        d = random.randint(1, 100)
        bot.send_message(call.message.chat.id,
                         f'Решите мой пример: {o} {s} {d} = ?\n🤖 Просто отправьте мне свой ответ 👇')  # бот отправляет сообщение

        markup3 = types.InlineKeyboardMarkup(row_width=1)  # кнопка в сообщение
        markup3.add(
            types.InlineKeyboardButton('Следующий пример', callback_data='next_middle1'))  # текст на кнопке в сообщение

        markup4 = types.InlineKeyboardMarkup()  # кнопка в сообщение
        markup4.add(types.InlineKeyboardButton('Попробовать снова',
                                               callback_data='next_middle2'))  # текст на кнопке в сообщение

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)  # x=текст с клавиатуры
            if x == (o + d):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup3)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup4)

        bot.register_next_step_handler(call.message, message_input)

    if call.data == 'next_hard1' or call.data == 'next_hard2':
        y = random.randint(1, 500)
        s = ('+')
        i = random.randint(1, 500)
        bot.send_message(call.message.chat.id,
                         f'Решите мой пример: {o} {s} {d} = ?\n🤖 Просто отправьте мне свой ответ 👇')  # бот отправляет сообщение

        markup5 = types.InlineKeyboardMarkup(row_width=1)  # кнопка в сообщение
        markup5.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_hard1'))  # текст на кнопке в сообщение

        markup6 = types.InlineKeyboardMarkup()  # кнопка в сообщение
        markup6.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_hard2'))  # текст на кнопке в сообщение

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)  # x=текст с клавиатуры
            if x == (o + d):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup5)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup6)

        bot.register_next_step_handler(call.message, message_input)


# region Команда START
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Ваш user ID: `{message.chat.id}`', parse_mode='Markdown')#бот отправляет сообщение "...", делает все буквы маленькими

    first_name = message.from_user.first_name
    message_text = f'Привет *{first_name}*! Этот бот помогает тренировать устный счет в уме, просто выбери нужный уровень сложности 👇\n\n' \
                   f'Чтобы найти автора, воспользуйтесь [ссылкой](https://t.me/lizzerd18).'


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Начальный уровень')#кнопка на клавиатуре
    btn2 = types.KeyboardButton('Средний уровень')
    btn3 = types.KeyboardButton('Сложный уровень')
    markup.add(btn1, btn2, btn3)


    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
# endregion Команда START

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Начальный уровень":
        a = random.randint(1, 30)
        s = ('+')
        b = random.randint(1, 30)
        bot.send_message(message.chat.id, f'Решите мой пример: {a} {s} {b} = ?\n🤖 Просто отправьте мне свой ответ 👇')

        markup1 = types.InlineKeyboardMarkup(row_width=1)
        markup1.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_simple1'))

        markup2 = types.InlineKeyboardMarkup(row_width=1)
        markup2.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_simple2'))

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)
            if x == (a + b):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup1)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup2)
        bot.register_next_step_handler(message, message_input)

    elif get_message_bot == "Средний уровень":
        o = random.randint(1, 100)
        s = ('+')
        d = random.randint(1, 100)
        bot.send_message(message.chat.id, f'Решите мой пример: {o} {s} {d} = ?\n🤖 Просто отправьте мне свой ответ 👇')

        markup3 = types.InlineKeyboardMarkup(row_width=1)
        markup3.add(types.InlineKeyboardButton('Следующий пример', callback_data ='next_middle1'))

        markup4 = types.InlineKeyboardMarkup()
        markup4.add(types.InlineKeyboardButton('Попробовать снова', callback_data ='next_middle2'))

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            q = int(message.text)
            if q == (o + d):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup3)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup4)

        bot.register_next_step_handler(message, message_input)

    elif get_message_bot == "Сложный уровень":
        y = random.randint(1, 500)
        s = ('+')
        i = random.randint(1, 500)
        bot.send_message(message.chat.id, f'Решите мой пример: {y} {s} {i} = ?\n🤖 Просто отправьте мне свой ответ 👇')

        markup5 = types.InlineKeyboardMarkup(row_width=1)
        markup5.add(types.InlineKeyboardButton('Следующий пример', callback_data='next_hard1'))

        markup6 = types.InlineKeyboardMarkup(row_width=1)
        markup6.add(types.InlineKeyboardButton('Попробовать снова', callback_data='next_hard2'))

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = int(message.text)
            if x == (y + i):
                bot.send_message(message.chat.id, f'Молодец, верный ответ 👍', reply_markup=markup5)
            else:
                bot.send_message(message.chat.id, 'Ответ неверный 😢', reply_markup=markup6)

        bot.register_next_step_handler(message, message_input)

    else:
        bot.send_message(message.chat.id, '🤖 я не знаю как Вам ответить на это..')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)