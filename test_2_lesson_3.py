# Описание данных пользователя
def character_person():
    name = input('enter your name:  ')
    surname = input('enter your surname:  ')
    birth_year = input('enter your birth_year:  ')
    city = input('enter your city:  ')
    e_mail = input('enter your e_mail:  ')
    phone = input('enter your phone:  ')
    x = '  '
    s_full = name + x + surname + x + birth_year + x + city + x + e_mail + x + phone
    return s_full

result = character_person()
print(result)
