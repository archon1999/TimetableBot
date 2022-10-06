import datetime

from telebot import TeleBot
from django.utils import timezone

import config

from backend.tasks import send_schedule


bot = TeleBot(
    token=config.TOKEN,
    num_threads=3,
    parse_mode='HTML',
)


@bot.message_handler(commands=['timetable'])
def message_handler(message):
    try:
        weekday = int(message.text.split()[1])
    except Exception:
        current_tz = timezone.get_default_timezone()
        weekday = datetime.datetime.now(current_tz).weekday() + 1

    send_schedule(weekday, message.chat.id)


if __name__ == "__main__":
    import locale
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    print(bot.get_me())
    # bot.polling()
    bot.infinity_polling()
