def month_to_season(n):
    if n == 12 or n == 1 or n == 2:
        return ('Зима')
    elif n == 3 or n == 4 or n == 5:
        return ('Весна')
    elif n == 6 or n == 7 or n == 8:
        return ('Лето')
    elif n == 9 or n == 10 or n == 11:
        return ('Осень')
    else:
        return ('Укажите номер месяца')


print(month_to_season(int(input('Введите номер месяца: '))))
