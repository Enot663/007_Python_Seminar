# a = int(input())
# b = int(input())
# c = int(input())
# # d = int(input())
# if a < b < c or a > b > c:
#     print(b)
# elif b < a < c or b > a > c:
#     print(a)
# else:
#     print(c)

# Количество дней

# month = int(input())
# if month == 2:
#     print("28")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print('30')
# else:
#     print('31')

# Церемония взвешивания

# weight = int(input())
# if weight < 60:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# elif 64 <= weight < 69:
#     print('Полусредний вес')

# Самописный калькулятор
# a = int(input())
# b = int(input())
# c = str(input())
# if c == '*':
#     print(a * b)
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/' and b == 0:
#     print('На ноль делить нельзя!')
# elif c != '/' and c != '-' and c != '*' and c != '+':
#     print('Неверная операция')
# else:
#     print(a / b)

# Виннипух

def find_rhythm(text: str):
    phrases = text.split()   # разбили текст на фразы
    phrases_vow = []   # пустой список для фраз, очищенных от согласных
    for i in phrases:   # каждую фразу фильтруем от согласных
        phrases_vow.append(list(filter(lambda x: x in 'аеиоуэюя', list(i))))
    result_list = map(lambda x: len(x) == len(phrases_vow[0]), phrases_vow)
    return all(result_list)
puffing = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if find_rhythm(puffing):
    print('Парам пам-пам')
else:
    print('Пам парам')


# Цветовой микшер





