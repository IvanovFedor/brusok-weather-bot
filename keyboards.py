import telebot


main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=10)
main.row('Погода', 'Прогноз')
main.row('Помощь')


error = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
error.row('Задать город', 'Назад')
