# --------------------------------задача1
# print("Hello, word")
# --------------------------------задача2
# print('4','8','15','16','23','42')
# --------------------------------задача3
# print('8')
# print('15')
# print('16')
# print('23')
# print('42')
# ---------------------------------робота в класі
# name = input('Як тебе звуть?')
# print('Привіт,', name)
# -------------------------------задача4
# print('**Sample Output*')
# print('"*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******"')
# --------------------робота в класі 13.06-------------------
# var = 0
# print(var == 0)
# var = input('Скільки?')
# print(var == 0)

# ws = 6
# bs = 2
# print(bs > 2*ws)
# читання двох чисел
# numbers1 = int(input('Введіть перше число: '))
# numbers2 = int(input('Введіть друге число: '))
# if (numbers1 > numbers2):
#     larger_number = numbers1
# else:
#     larger_number = numbers2
# print(larger_number)
# вибір більшого числа
#
# -----------------------------------------------
# Зчитуємо введене ім'я від користувача
#
# 18.06.2024 робота в класі
#
# -----------------
# count = 1
# while count <= 5:
#     print(count)
#     count += 2
# ----------------------------
# stuff = ' '
# while True:
#     print('String [type q to quit]:')
#     stuff = input()
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())
# print('Thank you!')
# --------------------------
# name = ' '
# while True:
#     print("Who are you?")
#     name = input()
#     if name != 'Iryna':
#         continue
#     print('Hello, Iryna. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
# --------------------------
# print('My name is')
# for i in range(5):
#     print('Iryna Kushnirenko (' + str(i) + ')')
# for i in range(3, -4, -1):
#     print(i)
# --------------------------------
# ints = ['1', '2', '4', '5', '6']
# for int in ints:
#     print(int)
# HOMEWORK LESSON 5-6
# ----------------------------

# -----------------
# count = 1
# while count <= 5:
#     print(count)
#     count += 2
# ----------------------------
# stuff = ' '
# while True:
#     print('String [type q to quit]:')
#     stuff = input()
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())
# print('Thank you!')
# --------------------------
# name = ' '
# while True:
#     print("Who are you?")
#     name = input()
#     if name != 'Iryna':
#         continue
#     print('Hello, Iryna. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
# --------------------------
# print('My name is')
# for i in range(5):
#     print('Iryna Kushnirenko (' + str(i) + ')')
# for i in range(3, -4, -1):
#     print(i)
# --------------------------------
# ints = ['1', '2', '4', '5', '6']
# for int in ints:
#     print(int)
# HOMEWORK LESSON 5-6!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ----------------------------
# w = (15 < 25) and (9 < 12)
# print(w)
# a = (1 < 7) and (9 < 2)
# print(a)
# d = (7 == 7) or (1 == 3)
# print(d)
# j = 2 + 7 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
# print(j)
# # ------------------------------
# count = 1
# while count <= 10:
#     print(count)
#     count += 5
# ------------------------------
# stuff = ' '
# while True:
#     print('Для виходу натисни ____ [натисни 3 для виходу]:')
#     stuff = input()
#     if stuff == '3':
#         break
#     print(stuff.capitalize())
# print('ДЯКУЮ!')
# -------------------------------
# name = ' '
# while True:
#     print("Хто сьогодні з нами працює?")
#     name = input()
#     if name != 'Ірина':
#         continue
#     print('Привіт, Ірина, можливо ти і пароль знаєш?  (це твій улюблений колір)')
#     password = input()
#     if password == 'фіолетовий':
#         break
# print('Ну ти і молодець! Давай працювати)!')
# -----------------------------------------
# print('Моє хоббі?')
# for i in range(7):
#     print('Приготування їжі! (' + str(i) + ')')
# for i in range(10, 2, -1):
#     print(i)
# --------------------------
# квіти = ['піон', 'троянда', 'мак', 'гортензія', 'хризантема', 'волошки']
# for квітка in квіти:
#     print(квітка)
# ---------------------------------------
# word = 'інтерпритація'
# for letter in word:
#     print(letter)
# --------------------------------------
# ukraine_cities = {
#     'Західній Україні': 'Львів',
#     'Південній Україні': 'Одеса',
#     'Східній Україні': 'Харків',
#     'Північній Україні': 'Київ',
#     'Центральній Україні': 'Чернігів'
# }
#
# for region, city in ukraine_cities.items():
#     # print(city)
#     # print(region)
#   print('В', region, 'є чудове місто', city)
# ------------------------------------------
# favorite_movies = {
#     'peter': 'Shark',
#     'julia': 'The Godfather',
#     'max': 'La La Land',
#     'sophia': 'Inception'
# }
#
# for name in sorted(favorite_movies.keys()):
#     print(name.title() + ", thank you for sharing your favorite movie.")
# -----------------------------------------------
#


# ----ПРАКТИЧНА РОБОТА--------20.06.2024--------------
# ----1
# name = input('Як тебе звуть?')
# print('Привіт,', name)
# ----2
# Довжина = int(input('Введіть довжину прямокутника: '))
# Ширина = int(input('Введіть ширину прямокутника: '))
# Площа = Довжина * Ширина
# print('Площа прямокутника дорівнює', Площа)
# ----3
# radius = float(input('Введіть радіус кола: '))
# площа = 3.14 * radius ** 2
# print('Площа кола дорівнює', площа)
# ----4
# ціна = float(input('Введіть вартість товару: '))
# відсоток = float(input('Введіть відсоток знижки: '))
# знижка = ціна * (відсоток / 100)
# ціназізнижкою = ціна - знижка
# print('Вартість товару після знижки становить', ціназізнижкою, 'грн.')
# -----5
# днів = float(input('Введіть кількість днів: '))
# години = днів * 24
# print(днів, 'днів дорівнює', години, 'годин')
# ----6
# number1 = int(input('Введіть перше число: '))
# number2 = (int(input('Введіть друге число: ')))
# if number1 == number2:
#     print("Числа рівні")
# else:
#     print("Числа не рівні")
# ----7
# number1 = int(input('Введіть перше число: '))
# number2 = int(input('Введіть друге число: '))
# if number1 != number2:
#     print("Числа не рівні")
# else:
#     print("Числа рівні")
# ----8
# a = int(input('Введіть перше число: '))
# b = int(input('Введіть друге число: '))
# if a > b:
#     print("Перше число більше другого")
# else:
#     print("Перше число не більше другого")
# ----9
# a = int(input('Введіть перше число: '))
# b = int(input('Введіть друге число: '))
# if a >= b:
#     print("Перше число більше або дорівнює другому")
# else:
#     print("Перше число менше")
# ----10
# a = int(input('Введіть перше число: '))
# b = int(input('Введіть друге число: '))
# if a < b:
#     print("Перше число менше другого")
# else:
#     print("Перше число не менше другого")
# ----11
# a = int(input('Введіть перше число: '))
# b = int(input('Введіть друге число: '))
# if a <= b:
#     print("Перше число менше або дорівнює другому")
# else:
#     print("Перше число більше")
# ----12
# a = int(input('Введіть перше число: '))
# b = int(input('Введіть друге число: '))
# if a > b:
#     print('a більше за b')
# elif a < b:
#     print('a менше за b')
# else:
#     print('a дорівнює b')
# ----13
# x = int(input('Введіть число: '))
# if x % 2 == 0:
#     print('Число парне.')
# else:
#     print('Число непарне.')
# ----14
# досвід = int(input('Введіть ваш досвід роботи: '))
# if досвід >= 5:
#     print("Ви маєте гарний досвід і можете працювати у нас в команді.")
# else:
#     print("Ви ще не досягли рівня, який нам підходить! Розвивайтесь далі.")
# ----15
# weather = input('Яка погода зараз? (дощ, град, сніг, мокрий сніг): ').lower()
# if weather == 'дощ':
#     print("Зараз йде дощ.")
# elif weather == 'град':
#     print("Зараз йде град.")
# elif weather == 'сніг':
#     print("Зараз йде сніг.")
# elif weather == 'мокрий сніг':
#     print("Зараз йде мокрий сніг.")
# else:
#     print("Погода не відома.")
# ----16
# станморя = input('Який стан моря зараз? (тепле, чисте, дуже солоне, холодне): ')
# if станморя == 'тепле':
#     print("Море тепле і приємне для купання.")
# elif станморя == 'чисте':
#     print("Море чисте, без сміття і забруднень.")
# elif станморя == 'дуже солоне':
#     print("Море дуже солоне, можливо, смакується солонкою на губах.")
# elif станморя == 'холодне':
#     print("Море холодне, купатися в ньому може бути прохолодно.")
# else:
#     print("Стан моря не відомий або невірно введений.")
# ----17
# місяцьзаномером = int(input('Введіть номер місяця (1-12): '))
# if місяцьзаномером == 12 or місяцьзаномером == 1 or місяцьзаномером == 2:
#     сезон = 'зима'
# elif місяцьзаномером >= 3 and місяцьзаномером <= 5:
#     сезон = 'весна'
# elif місяцьзаномером >= 6 and місяцьзаномером <= 8:
#     сезон = 'літо'
# elif місяцьзаномером >= 9 and місяцьзаномером <= 11:
#     сезон = 'осінь'
# else:
#     сезон = 'невірний номер місяця'
# if сезон != 'невірний номер місяця':
#     print(f"Місяць з номером {місяцьзаномером} належить до пори року - {сезон}.")
# else:
#     print(f"Введений номер місяця не існує.")
# ----18
# вік = int(input('Скільки вам років? '))
# if вік < 18:
#     категорія = 'дитина або підліток'
# elif вік < 65:
#     категорія = 'доросла особа'
# else:
#     категорія = 'пенсіонер'
# print(f"Ваш вік {вік} років ви '{категорія}'.")
# ----19
# while True:
#     password = input('Введіть пароль (або "exit" для виходу): ')
#     if password == '123':
#         print('Доступ дозволено')
#         break
#     elif password.lower() == 'exit':
#         print('Доступ заборонено')
#         break
#     else:
#         print('Невірний пароль. Спробуйте ще раз.')
# ----20
# while True:
#     try:
#         n = int(input("Введіть невід'ємне ціле число n: "))
#         if n < 0:
#             print("Будь ласка, введіть невід'ємне ціле число.")
#         else:
#             break
#     except ValueError:
#         print("Будь ласка, введіть ціле число.")
#
# sum_numbers = 0
# for i in range(1, n + 1):
#     sum_numbers += i
#
# print("Сума всіх цілих чисел від 1 до", n, "дорівнює", sum_numbers, ".")
# ----21
# num = int(input('Введіть ціле число:') )
# if num  > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i ==0:
#                 is_prime = False
#         if is_prime:
#             print('Просте число')
#         else:
#             print('Не просте число')
# ----22
# n = int(input("Введіть ціле число n: "))
# sum_numbers: int = 0
# for i in range(1, n + 1):
#     sum_numbers += i
# print(f"Сума всіх цілих чисел від 1 до, {n}, дорівнює, {sum_numbers}")
# ----24
# n = input('Введіть послідовність чисел через пробіл:')
# m = n.split()
# k = 0
# for number_str in m:
#     k += int(number_str)
#
# average = k / len(m)
# print('Середнє арифметичне введених чисел:', average)
# ----25
# numbers = [10, 20, 30, 40, 50]
# user_number = input("Введіть число: ")
# if user_number in numbers:
#         print(f"Число {user_number} знаходиться у списку.")
# else:
#         print(f"Число {user_number} не знаходиться у списку.")



# робота по додатку
# first, _, third = set([1, 2, 3])
# print(first, third)
# зрізи
# city = 'Київ'
# print(city[1:])
# cities = ['Київ', 'Львів', 'Житомир']
# print(cities[1:])
# cities = ['Київ', 'Львів', 'Житомир']
# print((cities[:2]))
# print(cities[1:2])
# fruits = ['полуниця', 'малина', 'яблуко', 'груша', 'слива']
# print(fruits[::-3])
# bands = ['Ignea', 1914, 'паліндром']
# print(bands[1:])
# boolean_set = {bool([1, 2,3]), bool(()), True}
# print(len(boolean_set))
# pos_numbers = {1,1,2,2,3}
# numbers = [list(pos_numbers)]
# numbers.append(bool((0,)))
# print(numbers)
# nums = (1, '2', '3', 4)
# print('2' in nums[1::-1])
# list_a = [-1, -2, 0]
# index = list_a[0]
# index *= -1
# result = bool(list_a[index])

# РОБОТА НА ПАРІ 25.06.2024
# popular_sites = ['Google', 'Youtube', 'Facebook', 'Baidu.com', 'Yahoo', 'Amazon']
# for index in range(len(popular_sites)):
#     print(index, popular_sites [index])
# days = ['monday', 'tuesday', 'wensday']
# fruits = ['orange', 'apple', 'mango']
# drinks = ['coffe', 'tea', 'juice']
# desert = ['cake', 'ice-cream', 'pie', 'pudding']
# for day, frut, drink, desert in zip(days, fruits, drinks, desert):
#     print(day, 'drink', drink, 'eat', frut, 'enjoy', desert)
# english = 'Monday', 'Tuesday', 'Wensday'
# french = 'Lundi', 'Mardi', ('Mercredi')
# print(list(zip(english, french)))
# print(dict(zip(english, french)))french
# my_str_list = ['1', '2', '3', '4' ]
# resullt = []
# for item in my_str_list:
#     resullt.append(int(item))
# print(resullt)
# resullt = tuple()
# for item in my_str_list:
#     resullt += (item,)
# print(resullt)
# result = set()
# for item in my_str_list:
#     result.add(float(item))
# print(result)
# my_int_list = list(map(int, my_str_list))
# print(my_int_list)
# my_float_list = list(map(float, my_str_list))
# print(my_float_list)
# my_new_str_list = list(map(str, my_float_list))
# print(my_new_str_list)
# включення
# number_list = []
# for number in range(1, 6):
#     number_list.append(number)
# print(number_list)
# number_list = [number -1 for number in range(1,10)]
# print(number_list)
# a_list = [number for number in range(1,6) if number %2 == 0]
# print(a_list)
# word = 'Antarctica'
# letter_counts = {letter: word.count(letter) for letter in word}
# print(letter_counts)
# word = 'Antarctica'
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)
# x = sum(range(1,51))
# print(x)
# ДЗ на 02.07.2023 Приклади з лекції
# ---------------------------------------список 1-26 виведення парного числа
# number_list = [number for number in range(1, 26)]
# for index, value in enumerate(number_list, 1):
#     if value % 2 == 0:
#         print(index, value)
# ------------------------------------ значення та його ступінь
# a = [number for number in range(1, 7)]
# print(a)
# for index, value in enumerate(a, 1):
#     print(index, value**2)
# -------------------------------- створення словника
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# -------------------------
# boolean_dict = {"bool": [False, True], "bool": [True, False]}
# last_element = boolean_dict["bool"][-1]
#
# print(last_element is not True)
# --------------------------------
# initial_data = {"key": "value", "value": "key"}
#
# result = initial_data.pop("value")
# del initial_data[result]
#
# print(initial_data)
# -------------------------
# fictional_heroes = {'x-men': ["Фенікс"], 'thor': {"location": "Асгард"}}
#
# print(fictional_heroes.keys())
# # dict_keys(['x-men', 'thor'])
#
# print(fictional_heroes.values())
# # dict_values([['Фенікс'], {'location': 'Асгард'}])
#
# print(fictional_heroes.items())
# # dict_items([('x-men', ['Фенікс']), ('thor', {'location': 'Асгард'})])
# -------------------
# dict_a = {"1": "один"}
#
# print(1 in dict_a)
# -------------------
# short_list = [1, 2, 3]
# position = 5
# try:
#    short_list[position]
# except:
#    print('Need a position between 0 and', len(short_list)-1, 'but got', position)
# --------------------------------------
# try:
#    print(5/0)
# except ZeroDivisionError:
#    print("You can't divide by zero!")
# -------------------------------
# predators = ['tiger', 'wolf', 'bear']
# while True:
#    value = input('Position [q to quit]? ')
#    if value == 'q':
#        break
#    try:
#        position = int(value)
#        print(predators[position])
#    except IndexError as err:
#        print('Bad index:', position)
#    except Exception as other:
#        print('Something else broke:', other)
# def divide(x, y):
#    try:
#        result = x / y
#    except ZeroDivisionError:
#        print("Division by zero!")
#    else:
#        print("Result is", result)
#    finally:
#        print("End of the calculation.")
# divide(2, 1)
# divide(2, 0)
# --------------------------
# class IsNotTitleException(Exception):
#    pass
#
# try:
#    rooms = ['Kitchen', 'study', 'Hall', 'Bathroom']
#    for room in rooms:
#        if room.title() != room:
#            raise IsNotTitleException('Fault!')
#
# except IsNotTitleException as exc:
#    print(exc)







































