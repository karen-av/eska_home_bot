from contextlib import redirect_stderr
import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = types.KeyboardButton('Отопление')
    item1 = types.KeyboardButton('Связь и ТВ')
    item2 = types.KeyboardButton('Электричество')
    item3 = types.KeyboardButton('Септик')
    item4 = types.KeyboardButton('Вода')
    item5 = types.KeyboardButton('В начало')
    item6 = types.KeyboardButton('/start')
    markup.add(item0, item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\
        \nЯ {1.first_name},\
        \nЗдесь вы найдете различные инструкции по эксплуатации нашего дома."\
        .format(message.from_user, bot.get_me()), parse_mode='html',\
        reply_markup=markup)


    @bot.message_handler(content_types=('text'))
    def menu_listner(message):
        if message.chat.type == 'private':
            if message.text == 'Отопление':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Температура', callback_data = 'home_temp')
                item2 = types.InlineKeyboardButton('Теплый пол', callback_data = 'floor')
                markup.add(item1, item2)
                bot.send_message(message.chat.id, "Норм, как сам?", reply_markup=markup)
            elif message.text == 'Связь и ТВ':
                pass
            elif message.text == 'Электричество':
                pass
            elif message.text == 'Вода':
                pass    
            elif message.text == 'Ворота':
                pass
            elif message.text == 'В начало':
                print('ddd')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'home_temp':
                bot.send_message(call.message.chat.id, \
                    "В первом корридоре около котла отопления установлен пульт управления. \
                    С помощью клавиш установите нужную температуру.")
            elif call.data == 'floor':
                bot.send_message(call.message.chat.id, \
                    "В первом корридоре около котла отопления находится люк с железной дверкой. \
                    Откройте двурцу и с помощью термоголовки установите нужную температуру теплого \
                    пола в зимнем саду.\n\nТемпература теплого пола в ванных комнатах решгулируется \
                    с помощью индивидуальных пультов управления. Пульты расположенны в ванных комнатах. \
                    установите нужную температуру клавишами вверх и вниз.")
    
    except Exception as ex:
        print(ex)

bot.polling(none_stop=True)