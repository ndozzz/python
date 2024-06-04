def add_time(start, duration, start_day = None):
    week = {
        'sunday': 'Sunday',
        'monday':'Monday',
        'tuesday':'Tuesday',
        'wednesday':'Wednesday',
        'thursday':'Thursday',
        'friday': 'Friday',
        'saturday':'Saturday'
    }
    Splitted_start = start.replace(':',' ').split()
    Splitted_duration = duration.split(':')
    week_list = list(week.keys())

    start_time = (int(Splitted_start[0]) * 60) + int (Splitted_start[1]) + 720 if Splitted_start[2] == "PM" else int(Splitted_start[0]) * 60 + int (Splitted_start[1])

    duration_time = (int(Splitted_duration[0]) * 60) + int(Splitted_duration[1])

    total_time = start_time + duration_time

    days = 0
    if total_time / 1440 < 1:
        hour = total_time // 60
        minute = total_time % 60
    else:
        days = total_time // 1440
        hour = (total_time % 1440) // 60
        minute = (total_time % 1440) % 60

    mark = 'AM' if hour < 12 else 'PM'

    days_count = '' if days < 1 else '(next day)' if days == 1 else f'({days} days later)'

    if start_day:
        correct_day = week_list[(week_list.index(start_day.lower()) + days) % 7]
    
    if hour < 1:
        hour = 12
        mark = "AM"
    
    if hour > 12:
        hour = hour - 12
    
    if days > 0:
        new_time = f'{hour}:{str(minute).zfill(2)} {mark}, {week[correct_day]} {days_count}' if start_day else f'{hour}:{str(minute).zfill(2)} {mark} {days_count}'
    else:
        new_time = f'{hour}:{str(minute).zfill(2)} {mark}, {week[correct_day]}' if start_day else f'{hour}:{str(minute).zfill(2)} {mark}'

    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))

"""
start = '3:00 PM'
duration =  '200:00'
day = None
week = {
        'sunday': 'Sunday',
        'monday':'Monday',
        'tuesday':'Tuesday',
        'wednesday':'Wednesday',
        'thursday':'Thursday',
        'friday': 'Friday',
        'saturday':'Saturday'
    }
week_list = list(week.keys())
print(week_list)

Splitted_start = start.replace(':',' ').split()
Splitted_duration = duration.split(':')
print(Splitted_start)
start_time = (int(Splitted_start[0]) * 60) + int (Splitted_start[1]) + 720 if Splitted_start[2] == "PM" else int(Splitted_start[0]) * 60 + int (Splitted_start[1])

print(start_time)
print(Splitted_duration)
duration_time = (int(Splitted_duration[0]) * 60) + int(Splitted_duration[1])
print(duration_time)
total_time = start_time + duration_time
print(total_time)
days = 0
if total_time / 1440 < 1:
    hour = total_time // 60
    minute = total_time % 60
else:
    days = total_time // 1440
    hour = (total_time % 1440) // 60
    minute = (total_time % 1440) % 60

mark = 'AM' if hour < 12 else 'PM'

days_count = '' if days < 1 else '(next day)' if days == 1 else f'({days} days later)'

print(hour)
print(minute)
print(days)
print(days_count)
print(mark)
if day:
    correct_day = week_list[(week_list.index(day.lower()) + days) % 7]
    print(week[correct_day])

new_time = f'{hour}:{str(minute).zfill(2)} {mark}, {week[correct_day]} {days_count}' if day else f'{hour}:{str(minute).zfill(2)} {mark} {days_count}'
print(new_time)
"""