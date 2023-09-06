from django.test import TestCase

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
    print(time_choices) 
time_choice()

