a = float(input('Сколько часов в день ты учишься в будни? '))
b = float(input('Сколько часов в день ты учишься в выходные? '))
week_hours = a*5 + b*2
month_hours = week_hours * 4
if week_hours < 7: print(f'{week_hours} Slow pace')
elif 7 < week_hours < 12: print(f'{week_hours} Normal pace')
else: print(f'{week_hours} Strong pace')
print(f'Monthly hours: {month_hours}')