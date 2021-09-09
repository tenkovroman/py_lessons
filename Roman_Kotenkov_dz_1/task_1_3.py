percents_words_list = ['процент', 'процента', 'процентов']
for nums in range(1, 101):
	if nums % 10 == 1 and nums % 100 != 11:
		print(nums, percents_words_list[0])
	elif 2 <= nums % 10 <= 4:
		print(nums, percents_words_list[1])
	else:
		print(nums, percents_words_list[2])

