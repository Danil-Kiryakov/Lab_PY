#1
""" from random import *
#1.1
list1 = [randint(-100, 100) for _ in range(20)] #генерация пустого списка
print(list1)
#1.2
list2 = [x//2 if x % 2 == 0 else x * 2 for x in list1]
print(list2)
#1.3
i = 0
while i < len(list1):
    if list1[i] < 0:
        list1.insert(i + 1, 0) #вставляем 0 со сдвигом последующих элементов
        i += 2
    else:
        i += 1
print(list1)
#1.4
k1 = int(input(f"Введите значение k1: "))
k2 = int(input(f"Введите значение k2: "))
if k1 > k2: k1, k2 = k2, k1
for i in range(len(list1) - 1, -1, -1):
    if k1 <= list1[i] <= k2:
        del list1[i]
print(list1)
#1.5
for i in range(3):
    element = list1.pop(0)
    list1.append(element)
print(list1)
#1.6
list1.sort(reverse = True)
print(list1) """

#2
""" from random import *
list1 = []
for _ in range(10):
    word = str(input(f"Введите слово: "))
    list1.append(word)

word = choice(list1)

flag = True
while flag == True:
    chars = list(word)
    shuffle(chars)
    question = ''.join(chars)
    if word != question:
        flag = False

print(f"угадайте слово по анаграмме (у вас 3 попытки): {question}")

i = 3
while i > 0:
    answer = str(input(f"Введите ваш ответ: "))
    i -= 1
    if word == answer:
        print('Вы угадали загаданное слово')
        break
    else:
        print('Ответ неверный')
if i == 0:
    print('Попытки закончились') """

#3
'''temp = [-14, -16, -4, 1, 10, 16, 19, 18, 15, 2, -2, -13]

def temp_statistics(lst): #статистика
    """Принимает список среднемесячных температур.
    Возвращает кортеж: (средняя, максимальная, минимальная, количество)"""
    avg = round(sum(lst) / len(lst), 1)
    max_t = max(lst)
    min_t = min(lst)
    count = len(lst)
    return (avg, max_t, min_t, count)

def filter_temp(lst, threshold, above=True): #фильтрация
    """Принимает список температур, пороговое значение threshold и флаг above.
    Если above = True — возвращает список температур выше или равных threshold.
    Если above = False — возвращает список температур ниже threshold"""
    result = []
    for i in lst:
        if above:
            if i >= threshold:
                result.append(i)
        else:
            if i < threshold:
                result.append(i)
    return result


def farengeit(lst): #фильтрация
    """Принимает список температур в градусах Цельсия.
    Возвращает новый список, где температуры переведены в Фаренгейты.
    Формула: F = C * 9/5 + 32"""
    return [c * 9/5 + 32 for c in lst]

#Статистика
stats = temp_statistics(temp)
print("Статистика температур:")
print("Средняя температура:", stats[0])
print("Максимальная температура:", stats[1])
print("Минимальная температура:", stats[2])
print("Количество значений:", stats[3])

#Фильтрация
filtered = filter_temp(temp, 2, above=False)
print("\nТемпературы ниже 2:", filtered)

#Фаренгейты
faren = farengeit(temp)
print("\nТемпературы в Фаренгейтах:", faren)'''

#4
'''test_numbers = [
    "+7 (916) 123-45-67",
    "8-916-123-45-67",
    "9161234567",
    "89161234567",
    "+7 916 123 45 67",
    "12345",
    "791612345678",
    12345678901,
    " abc ",
]

def clean_number(number) -> str | None: #очистка номера от лишних символов
    """Очищает номер от лишних символов, оставляя только цифры
    Параметр number: номер в любом формате (строка или число)
    Возвращаем строку только из цифр или None, если произошла ошибка"""
    try:
        number_str = str(number) #преобразовываем в строку
        digits = "" #пустая строка
        for char in number_str: #проходим по строке
            if char.isdigit(): #если текущий символо цифра
                digits += char #добавляем в конец нашей пустой строки
        return digits
    except Exception: #если в блоке try произошла ошибка
        return None

def is_valid_number(digits): #проверка номера
    """Проверяет номер на допустимость
    Параметр digits: строка из цифр
    Возвращаем True если номер корректный, False если нет"""
    if digits is None: #если наша строка - None
        return False #номер некорректный

    if len(digits) != 10 and len(digits) != 11: #если в номере не 10 и не 11 цифр
        return False #номер некорректный

    if len(digits) == 11: #если в номере 11 цифр
        if digits[0] != "7" and digits[0] != "8": #первая цифра не 7 и не 8
            return False #номер некорректный

    if len(digits) == 10: #если в номере 10 цифр
        if digits[0] != "9": #первая цифра не 9
            return False #номер некорректный

    return True

def format_number(digits) -> str: #преобразование номера
    """Преобразовывает номер в стандартный вид: +7 (XXX) XXX-XX-XX
    Параметр digits: строка из 10 или 11 цифр
    Возвращаем отформатированную строку"""
    if len(digits) == 11: #если в номере 11 цифр
        if digits[0] == "7" or digits[0] == "8": #если первая цифра 7 или 8
            digits = digits[1:] #берём строку с 1 индекса
    # Собираем итоговую строку, склеивая части номера с нужными скобками и дефисами
    result = "+7 (" + digits[0:3] + ") " + digits[3:6] + "-" + digits[6:8] + "-" + digits[8:10]
    return result

result = [] #пустой результирующий список

for number in test_numbers: #проходим по всем номерам из исходного списка
    digits = clean_number(number) #очищаем
    if is_valid_number(digits): #если номер прошёл проверку на кореектность
        formatted = format_number(digits) #форматируем
        result.append(formatted) #дбавляем номер в результирующий список
    else: #если номер не прошёл проверку
        result.append("Некорректный номер") #добавляем в результирующий список сообщение об ошибке

for i in result: #проходим по готовому результирующему списку
    print(i) #выводим элементы'''