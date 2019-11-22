import datetime

path = 'path to database file'


def readFromDatabase(path):
    database = open(path, 'r')
    data = database.read()
    database.close()
    return data


def addToDatabase(path, data):
    database = open(path, 'a+')
    database.write("{}#".format(datetime.datetime.now().ctime()) + data)
    database.close()


def databaseEmpty(dataFromDatabase):
    if (dataFromDatabase != ''):
        return True
    else:
        return False


def showDataFromDatabase(data):
    lines = data.splitlines()
    for line in lines:
        date = line.split("#")[0]
        message = line.split("#")[1]
        print("'{}' was added on '{}'".format(message, date))


if databaseEmpty(readFromDatabase(path)):
    print("Your journal contains these entries: \n")
    showDataFromDatabase(readFromDatabase(path))
    print("\nAdd new entries")
else:
    print("Your journal doesn't contain any entries yet, add one now.")

while True:
    entry = input('Enter a message to be saved in the journal: ')
    choice = input(
        "Your message is '{}', are you sure you want to add this to the journal? [y/n]: ".format(entry))
    if choice == 'y' or choice == 'Y':
        addToDatabase(path, entry + "\n")
        print("Your entry was added in the journal.")
    elif choice == 'n' or choice == 'N':
        print("Your entry wasn't added in the journal.")

    allEntries = input(
        "\nDo you want to see all entries in the journal? [y/n]: ")
    if allEntries == 'y' or allEntries == 'Y':
        print("Your journal contains these entries: ")
        showDataFromDatabase(readFromDatabase(path))

    print("\nYou can now write a new message for the journal.")
