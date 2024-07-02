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