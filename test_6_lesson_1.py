a = int(input('enter your start km:  '))
b = int(input('enter your end km:  '))
i = 1  # start from one day
while a < b:
    a = a + a * 0.1
    i = i + 1
print('number days to great success:  ', i)
