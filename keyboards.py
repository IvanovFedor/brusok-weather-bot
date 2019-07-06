import telebot


main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=10)
main_keyboard.row('Погода', 'Прогноз')


error_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
error_keyboard.row('Задать город', 'Назад')
