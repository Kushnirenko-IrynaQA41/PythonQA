# def birthday_card():
#     print('Happy birthday!')
# birthday_card()

# def hungry():
#     return True
# if hungry():
#     print('Eat oat flakes!')
# else:
#     print('Drink water.')

# def echo(anything):
#     return anything
# print(echo('I enjoy travelling!'))

# def like(interest):
#     if interest == 'yoga':
#         return "I quite like " + interest + "."
#     elif interest == "football":
#         return "Yes, I play " + interest + "."
#     elif interest == 'guitar':
#         return "Yes, I play the " + interest + "."
#     else:
#         return "I'm interested in " + interest + "."
# story = like('photography')
# print(story)
# story = like('yoga')
# print(story)
# story = like('football')
# print(story)
# story = like('guitar')
# print(story)

# def do_nothing():
#     pass
# print(do_nothing())

# def is_none(thing):
#     if thing is None:
#         print("It's None")
#     elif thing:
#         print("It's True")
#     else:
#         print("It's False")
# is_none(None)
# is_none(True)
# is_none(False)
# is_none(0)
# is_none(0.0)
# is_none(())
# is_none([])
# is_none({})
# is_none(set())


# def music(terminology, musician, genre):
#     return {'terminology': terminology, 'musician': musician, 'genre': genre}
# print(music('tune', 'guitarist', 'blues'))
# print(music(terminology='tune', musician='guitarist', genre='blues'))

# def describe_pet(pet_name, animal_type='parrot'):
#     print("I have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet(pet_name='Jack Sparrow')
# describe_pet(pet_name, animal_type='guinea pig')
# def print_days(*args):
#     print('Get ready:', args)
# print_days('Wednesday', 'Thursday', 'Friday', 'Weekend...')

# def print_travel(required1, required2, *args):
#     print('For train travel is required:', required1)
#     print('For train travel is required too:', required2)
#     print('All the rest:', args)
# print_travel('return ticket', 'train', 'carriage', 'seat', 'luggage rack')

# def print_character(**kwargs):
#     print('Person\'s characteristics:', kwargs)
# print_character(emotions='cheerful', sense='happy', look='slim')

# months = [(1, 'January'), (9, 'September'), (7, 'July'), (4, 'March')]
# print(sorted(months, key=lambda x: x[1]))
# print(sorted(months))
# урок 04.07.2024
#
# animal = 'kangaroo'
# def print_global():
#     print('inside print_global:', animal)
# print('at the top level:', animal)
# print_global()
# ------------------------------------
animal = 'kangaroo'
# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'giraffe'
#     print('after the change:', animal)
# change_and_print_global()
# ---------------------------------------
# def change_local():
#     animal = 'giraffe'
#     print('inside change_local:', animal, id(animal))
# change_local()
# print(animal)
# print(id(animal))
# -------------------------
# def change_and_print_global():
#     global animal
#     animal = 'giraffe'
#     print('inside change_and_print_global:', animal)
# print(animal)
# change_and_print_global()
# print(animal)
# ----------------------------------------

# def change_local():
#     animal = 'giraffe' # локальна змінна
#     print('locals:', locals())
# print(animal)
# change_local()
# print('locals:', locals())
# print('globals:', globals())
# print(animal)
# import random
# # for i in range(5):
# #     print(random.randint(1, 10))
# from random import randint, random
# for i in range(5):
#     print(randint(1, 10))
# print(random())
# import math
# print(math.fabs(-221.1))
#
# print(math.floor(56.8))
#
# print(math.ceil(38.3))
#
# print(math.factorial(7))
#
# print(math.pow(4, 3))
#
# print(math.sqrt(256))
#
# print(math.radians(180))
#
# print(math.degrees(math.pi))
# -----------------------
# import string
# s = 'It was nice talking to you! Thank you!'
# print(s)
# print(string.capwords(s))
# ------------------------------
# import inspect
# import string
#
# def is_str(value):
#     return isinstance(value, str)
#
# for name, value in inspect.getmembers(string, is_str):
#     if name.startswith('_'):
#         continue
#     print('{0} = {1}'.format(name, repr(value)))
# ------------------------------------------
# from collections import Counter
# birds = ['stork', 'sparrow', 'woodpecker', 'owl', 'woodpecker', 'sparrow', 'sparrow']
# birds_counter = Counter(birds)
# print(birds_counter)
# print(birds_counter['woodpecker'])
# print(birds_counter['sparrow'])
# --------------------------------
# from collections import Counter
# birds = ['stork', 'sparrow', 'woodpecker', 'owl', 'woodpecker', 'sparrow', 'sparrow']
# birds_counter = Counter(birds)
# other_birds = ['flamingo', 'nightingale', 'stork', 'sparrow']
# for bird in other_birds:
#     print('{0} : {1}'.format(bird, birds_counter[bird]))
# --------------------------
# from collections import OrderedDict
# from pprint import pprint
# regions = OrderedDict([
#     ('mountains', 'Himalayas'),
#     ('sands', 'Sahara'),
#     ('rivers', 'Yangtze')
# ])
# print(regions)
# pprint(regions)
# ----------------------------
