a = float(input('Сколько часов в день ты учишься в будни? '))
b = float(input('Сколько часов в день ты учишься в выходные? '))
week_hours = a*5 + b*2
month_hours = week_hours * 4
print(f'Weekly hours: {week_hours}')
if week_hours < 7: print('Pace: slow pace')
elif 7 < week_hours < 12: print('Pace: normal pace')
else: print('Pace: strong pace')
print(f'Monthly hours: {month_hours}')