# 1-----------------
# a1 = (15 > 8) and (2 == 9)
# print("(15 > 8) and (2 == 9) =", a1)
#
# a2 = not (2 > 1)
# print("not (2 > 1) =", a2)
#
# a3 = (6 > 3) or (8 == 7)
# print("(6 > 3) or (8 == 7) =", a3)
#
# a4 = not ((9 > 4) or (3 == 4))
# print("not ((9 > 4) or (3 == 4)) =", a4)
#
# a5 = (True and True) and (True == False)
# print("(True and True) and (True == False) =", a5)
#
# a6 = (not False) or (not True)
# print("(not False) or (not True) =", a6)
# 2----------------------------
# weather_forecast = input("Please enter the weather forecast (sun, rain, etc.): ")
# if weather_forecast == "sun":
#     print("What a beautiful day!")
# elif weather_forecast == "rain":
#     print("Take an umbrella!")
# else:
#     print("The sun’s just gone in!")
# 3-----------------------------
# points_color = input("Please enter the points color (green, yellow, red): ")
# if points_color == "green":
#     print("Player earned 5 points!")
# elif points_color == "yellow":
#     print("Player earned 10 points!")
# elif points_color == "red":
#     print("Player earned 15 points!")
# else:
#     print("Invalid color entered.")
# 4-------------------------------
# age = int(input("Введіть ваш вік: "))
# if age < 2:
#     print("baby")
# elif 2 <= age < 4:
#     print("kid")
# elif 4 <= age < 13:
#     print("child")
# elif 13 <= age < 20:
#     print("teenager")
# elif 20 <= age < 65:
#     print("grown-up")
# else:
#     print("senior")
# 5-------------------------------------------
# favorite_fruits = ["яблуко", "манго", "персик"]
# fruit = input("Введіть назву фрукту: ")
# if fruit in favorite_fruits:
#     print(f"Ти справді полюбляєш {fruit}!")
# else:
#     print(f"{fruit} не входить до списку улюблених фруктів.")
# 6---------------------------------------------
# список = [5, 4, 3, 2, 1, 0, 'GO!']
# for item in список:
#     print(item)
# або так (Функція len() повертає кількість елементів у списку.)
# список = [5, 4, 3, 2, 1, 0, 'GO!']
# for s in range(len(список)):
#     print(список[s])
# 7--------------------------------
# seasons = ['summer', 'autumn']
# months = ['july', 'november']
# movies = dict(zip(seasons, months))
# print(movies)
# 8------------------------------
# activity = {'business': 'manager', 'it': 'software developer', 'science': 'scientist'}
# for category, profession in activity.items():
#     print(f'{category}: {profession}')
# 9------------------------------
# парні_числа = list(range(0, 12, 2))
# print(парні_числа)
# 10--------------------------------
# степень2 = {num: num ** 2 for num in range(1, 11)}
# print(степень2)
# 11---------------------------------
# for a in range(1, 16):
#     print(a, end=' ')
# 12-----------------------------
# numbers = list(range(1, 1000001))
# print("Мінімальне число в списку:", min(numbers))
# print("Максимальне число в списку:", max(numbers))
# total_sum = sum(numbers)
# print("Сума усіх чисел у списку:", total_sum)
# 13------------------------------
# num = list(range(1, 26, 2))
# for number in num:
#     print(number)
# 14---------------------------
# куб = [num ** 3 for num in range(1, 11)]
# for cube in куб:
#     print(cube, end=' ')
# 15----------------------------
# number = 3
# while number <= 60:
#     print(number)
#     number += 1
# 16-----------------------
# def trees():
#     return ['poplar', 'willow', 'lime']
#
# tree_list = trees()
# print(tree_list)
# 17-----------------
# def favorite_book(title):
#     print(f"Одна з моїх улюблених книжок \"{title}\".")
#
# favorite_book("Віднесені вітром")
# 18-----------------------------------------------------
# def make_shirt(size, text):
#     print(f"Футболка розміру {size} з написом: {text}")
#
# # Виклик функції з позиційними аргументами
# make_shirt('M', 'Hello, World!')
# # Виклик функції з іменованими аргументами
# make_shirt(size='L', text='Python Rocks!')
# # функція з аргументами за замовчуванням
# def make_shirt(size='XL', text='I love Python!'):
#     print(f"Футболка розміру {size} з написом: {text}")
#
# make_shirt()
# 19-----------------------------------------------
# def city_country(city, country):
#     return f"{city.title()}, {country.title()}"
#
# print(city_country('київ', 'україна'))
# print(city_country('нью-йорк', 'сша'))
# print(city_country('варшава', 'польща'))
# 20------------------------------------------------
# визначення MyException
# class MyException(Exception):
#     pass
#
# try:
#     raise MyException("This is my custom exception.")
# except MyException as e:
#     print(e)
# 21----------------------------------------
# def sum_numbers(num1, num2):
#     try:
#         result = int(num1) + int(num2)
#         print(f"Сума чисел {num1} і {num2} дорівнює {result}")
#     except TypeError:
#         print("Помилка: одне з введених значень не є числом.")
#
# while True:
#     try:
#         num1 = input("Введіть перше число: ")
#         num2 = input("Введіть друге число: ")
#         sum_numbers(num1, num2)
#         break
#     except ValueError:
#         print("Помилка: введіть числа коректно.")
#
# Задачі!!!!!
# 1--------------------------------------------
# users = ['Admin', 'Alex', 'Emma', 'John']
#
# if users:
#     for user in users:
#         if user == 'Admin':
#             print("Hello Admin, I hope you’re well.")
#         else:
#             print(f"Hello {user}, thank you for logging in again.")
# else:
#     print("We need to find some users!")
# 2------------------------------
# sides = int(input("Введіть кількість сторін (від 3 до 6): "))
#
# if sides == 3:
#     figure_name = "Трикутник"
# elif sides == 4:
#     figure_name = "Чотирикутник"
# elif sides == 5:
#     figure_name = "П'ятикутник"
# elif sides == 6:
#     figure_name = "Шестикутник"
# else:
#     figure_name = "Геометрична фігура з такою кількістю сторін не задано"
#
# print(figure_name)
# 3-----------------------------------------------
# numbers = list(range(1, 10))
#
# for number in numbers:
#     if number == 1:
#         suffix = "st"
#     elif number == 2:
#         suffix = "nd"
#     elif number == 3:
#         suffix = "rd"
#     else:
#         suffix = "th"
#
#     print(f"{number}{suffix}")
# 4---------------------------------
# number = int(input("Введіть ціле число: "))
#
# if number % 2 == 0:
#     print(f"Число {number} є парне.")
# else:
#     print(f"Число {number} є непарне.")
# 5------------------------------------
# month_days = {
#     "січень": 31,
#     "лютий": "28 або 29 ",
#     "березень": 31,
#     "квітень": 30,
#     "травень": 31,
#     "червень": 30,
#     "липень": 31,
#     "серпень": 31,
#     "вересень": 30,
#     "жовтень": 31,
#     "листопад": 30,
#     "грудень": 31
# }
# month = input("Введіть назву місяця: ")
# if month in month_days:
#     days = month_days[month]
#     print(f"У місяці {month} {days} днів.")
# else:
#     print("такого місяця не існує")
# 6------------------------------------------------
# year = int(input("Введіть рік (від 1900 до 3000): "))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Високосний рік.")
# else:
#     print("Звичайний рік.")
# 7--------------------------------------------
# while True:
#     try:
#         number = int(input("Введіть ціле число (для виходу введіть число >= 100): "))
#         if number < 10:
#             continue
#         elif number >= 100:
#             break
#         else:
#             print(number)
#     except ValueError:
#         print("Введено неправильне значення. Будь ласка, введіть ціле число.")
# 8-----------------------------------------------
#






























