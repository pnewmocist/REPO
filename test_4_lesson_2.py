phrase = input('write some sentences:  ')
my_list = phrase.split('_')
for my_list, el in enumerate(my_list, 1):
    print(my_list, el[:10])




