import json


if __name__ == '__main__':

    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    with open('birthdays.json', 'w') as open_file:
        json.dump(birthdays, open_file)

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for key in birthdays.keys():
        print(key)

    name = input("enter name:")
    birthday = birthdays.get(name, "name not on list!")

    print("{}'s birthday is {}.".format(name, birthday))