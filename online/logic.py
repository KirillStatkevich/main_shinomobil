from datetime import  datetime,timedelta
import telebot
bot=telebot.TeleBot('6271494419:AAHBj7uAFjE9wNewX4cc7t5CPLhJTky2_NU')




def datechoce():
    date_choices = []
    today = datetime.now().date()
    for i in range(4):
        date = today + timedelta(days=i)
        date_str = date.strftime('%Y-%m-%d')
        date_choices.append((date, date_str))
    return date_choices

def bot_main_message(name, phone_number,time,date,main_text,place):
    text=(f'У вас новая онлайн запись!!!\n\nФИО: {name};\nНомер телефона: {phone_number};\nАдрес: {place};\nДата и время: {date} в {time};\nКомментарий клиента: {main_text} ')
    bot.send_message(chat_id=-1001746313809, text=text)



def time_choice():
    time_choices = [('', 'Выберите время')]
    start_hour = 9
    start_minute = 0
    end_hour = 23
    delta_hour = 1
    delta_minute = 30
    while start_hour < end_hour:
        time_str = f'{start_hour:02}:{start_minute:02}'
        time_choices.append((time_str, time_str))
        start_minute += delta_minute
        start_hour += delta_hour
        if start_minute >= 60:
            start_minute -= 60
            start_hour += 1
    return time_choices
