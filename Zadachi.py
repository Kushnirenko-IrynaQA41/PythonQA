# 1.	Які результати обчислення таких виразів
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
# 2.	Напишіть код, який виводить різні повідомлення, в залежності від значення, що зберігається у змінній weather_forecast
# weather_forecast = input("Please enter the weather forecast (sun, rain, etc.): ")
# if weather_forecast == "sun":
#     print("What a beautiful day!")
# elif weather_forecast == "rain":
#     print("Take an umbrella!")
# else:
#     print("The sun’s just gone in!")
# 3.	Створіть програму, яка виводить повідомлення про кількість очок
# points_color = input("Please enter the points color (green, yellow, red): ")
# if points_color == "green":
#     print("Player earned 5 points!")
# elif points_color == "yellow":
#     print("Player earned 10 points!")
# elif points_color == "red":
#     print("Player earned 15 points!")
# else:
#     print("Invalid color entered.")
# 4.	Напишіть ланцюжок if-elif-else для визначення віку людини
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
# 5.	Створіть список трьох своїх улюблених фруктів і назвіть його favorite_fruits
# favorite_fruits = ["яблуко", "манго", "персик"]
# fruit = input("Введіть назву фрукту: ")
# if fruit in favorite_fruits:
#     print(f"Ти справді полюбляєш {fruit}!")
# else:
#     print(f"{fruit} не входить до списку улюблених фруктів.")
# 6.	Використайте цикл for
# список = [5, 4, 3, 2, 1, 0, 'GO!']
# for item in список:
#     print(item)
# 7.	Використайте функцію zip(),
# seasons = ['summer', 'autumn']
# months = ['july', 'november']
# movies = dict(zip(seasons, months))
# print(movies)
# 8.	Використайте відомі вам структури коду для виведення ключів
# activity = {'business': 'manager', 'it': 'software developer', 'science': 'scientist'}
# for category, profession in activity.items():
#     print(f'{category}: {profession}')
# 9.	Використайте включення списку
# парні_числа = list(range(0, 12, 2))
# print(парні_числа)
# 10.	Використайте включення словника, щоб створити словник squares
# степень2 = {num: num ** 2 for num in range(1, 11)}
# print(степень2)
# 11.	Використайте цикл for
# for a in range(1, 16):
#     print(a, end=' ')
# 12.	Створіть список чисел від 1 до 1 000 000. Скористайтеся функціями min() і max()
# numbers = list(range(1, 1000001))
# print("Мінімальне число в списку:", min(numbers))
# print("Максимальне число в списку:", max(numbers))
# total_sum = sum(numbers)
# print("Сума усіх чисел у списку:", total_sum)
# 13.	Cкористайтеся третім аргументом функції range()
# num = list(range(1, 26, 2))
# for number in num:
#     print(number)
# 14.	Створіть список перших 10 кубів
# куб = [num ** 3 for num in range(1, 11)]
# for cube in куб:
#     print(cube, end=' ')
# 15.	Cтворіть список чисел у діапазоні від 3 до 60
# number = 3
# while number <= 60:
#     print(number)
#     number += 1
# 16.	Визначте функцію trees
# def trees():
#     return ['poplar', 'willow', 'lime']
#
# tree_list = trees()
# print(tree_list)
# 17.	Напишіть функцію favorite_book(),
# def favorite_book(title):
#     print(f"Одна з моїх улюблених книжок \"{title}\".")
#
# favorite_book("Віднесені вітром")
# 18.	Напишіть функцію make_shirt(),
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
# 19.	Напишіть функцію city_country(),
# def city_country(city, country):
#     return f"{city.title()}, {country.title()}"
#
# print(city_country('київ', 'україна'))
# print(city_country('нью-йорк', 'сша'))
# print(city_country('варшава', 'польща'))
# 20.	Визначте виняток, який називається MyException
# визначення MyException
# class MyException(Exception):
#     pass
#
# try:
#     raise MyException("This is my custom exception.")
# except MyException as e:
#     print(e)
# 21 TypeError
# def sum_numbers(num1, num2):
#     try:
#         result = int(num1) + int(num2)
#         print(f"Сума чисел {num1} і {num2} дорівнює {result}")
#     except TypeError:
#         print("Помилка: одне з введених значень не є числом.")
# num1 = input("Введіть перше число: ")
# num2 = input("Введіть друге число: ")
# sum_numbers(num1, num2)
#
# Задачі!!!!!
# 1.	Виведіть вітальне повідомлення для кожного користувача після його входу на сайт
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
# users.clear()
# if users:
#     for user in users:
#         if user == 'Admin':
#             print("Hello Admin, I hope you’re well.")
#         else:
#             print(f"Hello {user}, thank you for logging in again.")
# else:
#     print("We need to find some users!")
# 2.	Визначте назву геометричної фігури за введеною
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
# 3.	Порядкові числівники у англійській мові закінчуються суфіксом
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
# 4.	Зчитайте ціле число введене користувачем і виведіть
# number = int(input("Введіть ціле число: "))
#
# if number % 2 == 0:
#     print(f"Число {number} є парне.")
# else:
#     print(f"Число {number} є непарне.")
# 5.	Зчитайте назву місяця від користувача як рядок
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
# 6.	Потрібно визначити, чи є даний рік високосним
# year = int(input("Введіть рік (від 1900 до 3000): "))
#
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Високосний рік.")
# else:
#     print("Звичайний рік.")
# 7.	Зчитайте зі стандартного вводу цілі числа
# total = 0
#
# while True:
#     try:
#         num = int(input("Введіть ціле число (для завершення введіть 0): "))
#         if num == 0:
#             break
#         total += num
#     except ValueError:
#         print("Введено неправильне значення. Будь ласка, введіть ціле число.")
#
# print("Загальна сума введених чисел:", total)
# 8.	Зчитайте цілі числа, які вводить користувач, по одному числу у рядку
# while True:
#     try:
#         num = int(input("Введіть ціле число: "))
#         if num > 100:
#             break
#         elif num < 10:
#             continue
#         else:
#             print(num)
#     except ValueError:
#         print("Введено неправильне значення. Будь ласка, введіть ціле число.")
# 9.	Напишіть простий калькулятор
# def calculator():
#     try:
#         first_num = float(input("Введіть перше число: "))
#         second_num = float(input("Введіть друге число: "))
#         operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")
#
#         if operation == "+":
#             result = first_num + second_num
#         elif operation == "-":
#             result = first_num - second_num
#         elif operation == "/":
#             try:
#                 result = first_num / second_num
#             except ZeroDivisionError:
#                 return "Division by zero!"
#         elif operation == "*":
#             result = first_num * second_num
#         elif operation == "mod":
#             try:
#                 result = first_num % second_num
#             except ZeroDivisionError:
#                 return "Division by zero!"
#         elif operation == "pow":
#             result = first_num ** second_num
#         elif operation == "div":
#             try:
#                 result = first_num // second_num
#             except ZeroDivisionError:
#                 return "Division by zero!"
#         else:
#             return "Неправильна операція!"
#
#         return f"Результат: {result}"
#
#     except ValueError:
#         return "Введено неправильне значення. Будь ласка, введіть числа."
#
# print(calculator())
# 10 Користувач вводить номінал банкноти
# банкноти = {
#     1: "Володимир Великий",
#     2: "Ярослав Мудрий",
#     5: "Богдан Хмельницький",
#     10: "Іван Мазепа",
#     20: "Іван Франко",
#     50: "Михайло Грушевський",
#     100: "Тарас Шевченко",
#     200: "Леся Українка",
#     500: "Григорій Сковорода"
# }
# def знайти_особу_за_банкнотою():
#     try:
#         номінал = int(input("Введіть номінал банкноти: "))
#         if номінал in банкноти:
#             print(f"На банкноті номіналом {номінал} гривень зображений {банкноти[номінал]}.")
#         else:
#             print("Банкноти з таким номіналом не існує.")
#     except ValueError:
#         print("Введено неправильне значення. Будь ласка, введіть ціле число.")
#
# знайти_особу_за_банкнотою()
# 11 шахової фігури
# def determine_square_color():
#     try:
#         column = input("Введіть літеру стовпця (a-h): ").strip().lower()
#         row = int(input("Введіть номер рядка (1-8): "))
#
#         # Перевіряємо, чи введені координати знаходяться на дошці
#         if column not in 'abcdefgh' or not (1 <= row <= 8):
#             print("Неправильні координати")
#             return
#         column_index = ord(column) - ord('a')
#         is_black_square = (column_index % 2 == row % 2)
#
#         if is_black_square:
#             print("Квадрат має колір white")
#         else:
#             print("Квадрат має колір black")
#
#     except ValueError:
#         print("Неправильний формат введення для номеру рядка.")
#
# determine_square_color()
# 12 паліндромом
# def check_palindrome():
#     while True:
#         user_input = input("Введіть рядок для перевірки (або введіть 'escape' для виходу): ")
#         if user_input.lower() == 'escape':
#             break
#         # Видаляємо з рядка пробіли і переводимо у нижній регістр
#         s = user_input.replace(" ", "").lower()
#         # Перевіряємо, чи є рядок паліндромом
#         if s == s[::-1]:
#             print(f"'{user_input}' is a palindrome.")
#         else:
#             print(f"'{user_input}' is not a palindrome.")
#
# # Викликаємо функцію для перевірки рядка
# check_palindrome()

# 13 таблиця множення
# def multiplication_table():
#     try:
#         size = int(input("Введіть розмір таблиці множення (кількість рядків і стовпців): "))
#         if size <= 0:
#             print("Розмір таблиці повинен бути додатнім числом.")
#             return
#
#         for i in range(1, size + 1):
#             for j in range(1, size + 1):
#                 print(f"{i} * {j} = {i * j}")
#             print()  # Порожній print для розділення рядків таблиці
#
#     except ValueError:
#         print("Будь ласка, введіть коректне число.")
#
#
# # Виклик функції для тестування
# multiplication_table()
# 14 день програміста
# def progr_day():
#     try:
#         n = int(input('Введіть номер дня (n): '))
#         if n != 256:
#             return print('У 2017 році День програміста припадає на 256-й день.')
#
#         days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         day_of_year = 0
#         month = 0
#
#         for i in range(len(days_in_months)):
#             day_of_year += days_in_months[i]
#             if day_of_year >= n:
#                 month = i + 1
#                 day = n - (day_of_year - days_in_months[i])
#                 return print(f'День програміста (256-й день) у 2017 році: {day} вересня')
#
#     except ValueError:
#         print('Будь ласка, введіть дійсний номер дня.')
#
# # Виклик функції
# progr_day()
#15 шифр Цезаря
# def caesar_cipher(message, shift):
#     encrypted_message = ""
#
#     for char in message:
#         if char.isalpha():
#             shift_amount = shift % 26
#             if char.islower():
#                 base = ord('a')
#             else:
#                 base = ord('A')
#
#             # Обчислення нової позиції символу
#             new_position = (ord(char) - base + shift_amount) % 26
#             new_char = chr(base + new_position)
#             encrypted_message += new_char
#         else:
#             encrypted_message += char
#
#     return encrypted_message
#
#
# # Отримання вхідних даних від користувача
# message = input("Введіть повідомлення: ")
# shift = int(input("Введіть зсув: "))
#
# # Шифрування повідомлення
# result = caesar_cipher(message, shift)
# print("Зашифроване повідомлення:", result)

# 16 генерує випадковий пароль
# /////////////////////////////////
# import random
#
# def generate_password():
#     # Випадково визначаємо довжину паролю від 7 до 10 символів
#     length = random.randint(7, 10)
#
#     # Генеруємо пароль з випадкових символів від 33 до 126
#     password = ""
#     for _ in range(length):
#         random_ascii = random.randint(33, 126)
#         password += chr(random_ascii)
#
#     return password
#
# if __name__ == "__main__":
#     password = generate_password()
#     print("Випадковий пароль:", password)

# 17 генерує випадкове число, а користувач повинен вгадати число
# /////////////////////////////////////////////////////
# import random
#
# def guess_the_number():
#     # Генеруємо випадкове число від 1 до 100
#     number_to_guess = random.randint(1, 100)
#     attempts = 10  # Кількість спроб
#
#     print("Вгадайте число від 1 до 100. У вас є 10 спроб.")
#
#     for attempt in range(1, attempts + 1):
#         try:
#             user_guess = int(input(f"Спроба {attempt}: "))
#         except ValueError:
#             print("Будь ласка, введіть дійсне число.")
#             continue
#
#         if user_guess < number_to_guess:
#             print("Загадане число більше.")
#         elif user_guess > number_to_guess:
#             print("Загадане число менше.")
#         else:
#             print(f"Вітаємо! Ви вгадали число {number_to_guess} з {attempt} спроби!")
#             break
#     else:
#         print(f"Ви використали всі спроби. Загадане число було {number_to_guess}.")
#
# if __name__ == "__main__":
#     guess_the_number()
# 18 «Камінь, Ножиці, Папір»
# //////////////////////////////////////////
# import random
#
# def rock_paper_scissors():
#     def get_user_choice():
#         choices = ["камінь", "ножиці", "папір"]
#         choice = input("Виберіть камінь, ножиці або папір: ").lower()
#         while choice not in choices:
#             print("Неправильний вибір. Будь ласка, виберіть камінь, ножиці або папір.")
#             choice = input("Виберіть камінь, ножиці або папір: ").lower()
#         return choice
#
#     def get_computer_choice():
#         choices = ["камінь", "ножиці", "папір"]
#         return random.choice(choices)
#
#     def determine_winner(user_choice, computer_choice):
#         if user_choice == computer_choice:
#             return "Нічия!"
#         elif (user_choice == "камінь" and computer_choice == "ножиці") or \
#              (user_choice == "ножиці" and computer_choice == "папір") or \
#              (user_choice == "папір" and computer_choice == "камінь"):
#             return "Ви виграли!"
#         else:
#             return "Ви програли!"
#
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()
#     print(f"Комп'ютер вибрав: {computer_choice}")
#     result = determine_winner(user_choice, computer_choice)
#     print(result)
#
# # Запускаємо гру
# rock_paper_scissors()

































