duration = int(input('Введите число: '))

if duration < 60:
	print(duration, 'сек')
elif 60 <= duration < 3600:
	minutes = duration // 60
	seconds = duration % 60
	print(minutes, 'мин', seconds, 'сек')
elif 3600 < duration < 86400:
	hours = duration // 3600
	minutes = duration // 60 % 60
	seconds = duration % 60
	print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
	days = duration // 86400
	hours = (duration % 86400) // 3600
	minutes = duration // 60 % 60
	seconds = duration % 60
	print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
