def bold(string):
    return '*' + string + '*'


def italic(string):
    return '_' + string + '_'


def system(string):
    return '`' + string + '`'


# При отправке сообщения указать в параметрах parse_mode='Markdown'
# Пример:
# bot.send_message(message.from_user.id, text, parse_mode='Markdown')

