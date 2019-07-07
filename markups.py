import telebot


main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=10)
main.row('Погода \U000026C5', 'Прогноз \U0001F4C5')
main.row('Помощь \U00002753')


error = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
error.row('Задать город \U0001F4CD', 'Назад \U0001F519')

