import json

if __name__ == '__main__':
    birthdays = {}
    with open('birthdays.json', 'r+') as jsonFile:
        birthdays = json.load(jsonFile)
        print("Welcome to the birthday dictionary. We know the birthdays of:")
        for key in birthdays.keys():
            print(key)

        name = input("enter name:")
        birthday = birthdays.get(name, "name not on list!")

        print("{}'s birthday is {}.".format(name, birthday))

        answer = input("Please add another name and birthday if you like:")

        name = answer.split(',')[0]
        birthday = answer.split(',')[1]
        birthdays[name] = birthday
        jsonFile.seek(0)
        json.dump(birthdays, jsonFile)
        jsonFile.truncate()




