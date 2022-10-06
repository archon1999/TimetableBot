import os
import calendar
import datetime

import telebot
from django.utils import timezone
from django_q.tasks import schedule, Schedule

from backend.templates import Messages
from backend.models import Lesson, filter_html

import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')


TOKEN = os.getenv('BOT_TOKEN')
GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID')


def schedule_preparation():
    weekday = datetime.datetime.now().weekday() + 1
    lessons = Lesson.lessons.filter(weekday=weekday)
    if not lessons.exists():
        return

    send_todays_schedule()
    func_name = 'backend.tasks.send_todays_schedule'
    time = lessons.first().time
    current_tz = timezone.get_default_timezone()
    first_lesson_time = datetime.datetime.now(current_tz).replace(
        hour=time.hour,
        minute=time.minute,
    )
    next_run = first_lesson_time - timezone.timedelta(hours=1)
    name = 'send-todays-schedule'
    schedule(func_name,
             name=name,
             schedule_type=Schedule.ONCE,
             next_run=next_run)


def send_todays_schedule():
    weekday = datetime.datetime.now().weekday() + 1
    send_schedule(weekday)


def send_schedule(weekday, chat_id=GROUP_CHAT_ID):
    lessons = Lesson.lessons.filter(weekday=weekday)
    lessons_info = str()
    for lesson in lessons:
        if lesson.room_number:
            room_number = f'<code>{lesson.room_number}</code>'
        else:
            room_number = Messages.REMOTELY

        lesson_name = lesson.name
        if lesson.schedule_type != Lesson.ScheduleType.FULL:
            lesson_name += ', ' + lesson.get_schedule_type_display()

        lesson_info = Messages.LESSON_INFO.format(
            lesson_name=lesson_name,
            time=lesson.time.strftime('%H:%M'),
            teacher_name=lesson.teacher_name,
            room_number=room_number,
        )
        if lesson.note:
            lesson_info += '\n<b>Примечание: </b>' + filter_html(lesson.note)

        lessons_info += lesson_info + '\n\n'

    if get_week_parity():
        week_parity = Messages.WEEK_PARITY_EVEN
    else:
        week_parity = Messages.WEEK_PARITY_ODD

    timetable_info = Messages.TIMETABLE.format(
        weekday=calendar.day_name[weekday-1],
        week_parity=week_parity,
        lessons_info=lessons_info,
    )
    bot = telebot.TeleBot(token=TOKEN, parse_mode='HTML')
    bot.send_message(chat_id, timetable_info)


def get_week_parity():
    days = (datetime.datetime.now() - datetime.datetime(2022, 10, 3)).days
    return (days // 7) % 2
