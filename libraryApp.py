library = {}
sorted_library = {}
given = {}
not_given = {}


def stripper(n):
    for i in range(len(n)):
        n[i] = n[i].strip()


def books():
    print('****************************')
    print('GIVEN: ', given)
    print('LIBRARY: ', library)
    print('NOT_GIVEN: ', not_given)
    print('****************************')


def addBook():
    inp = input('\"book\'s name\", \"book\'s number\", \"book\'s category\", \"book\'s placement\", \"book\'s author\", \"book\'s publishment year\"\n')
    param = inp.split(',')
    stripper(param)
    if (len(param) != 6):
        print('Can not add book to the system. Missing parameter(s).')
    elif ((param[1].isdigit() == False) or (param[5].isdigit() == False)):
        print('Can not add book to the system. Improper parameter(s).')
    else:
        library[param[0]] = []
        for i in range(len(param)):
            library[param[0]].append(param[i])
        not_given[param[0]] = []
        for i in range(len(param)):
            not_given[param[0]].append(param[i])
        print('{} has added to the system.'.format(param[0]))


def takeBook():
    inp = input(
        "\"book\'s name\"/ \"book\'s number\", \"id of the people who take it\"\n")
    param = inp.split(',')
    stripper(param)
    if (len(param) != 2):
        print('Can not give book. Missing parameter(s).')
    else:
        if (param[0].isdigit() == False):
            if ((param[0] in given.keys()) and (param[0] not in not_given.keys())):
                print('Can not give book. Someone has already taken it.')
            elif (param[0] not in library.keys()):
                print('Can not give book. There is no book like this in this system.')
            elif (param[0] not in given.keys() and (param[0] in not_given.keys())):
                new_list = not_given[param[0]]
                new_list.append(param[1])
                given[param[0]] = new_list
                not_given.pop(param[0])
                print('{} has given with no problem.'.format(param[0]))
        elif (param[0].isdigit() == True):
            name = findNumber(library, param[0])
            if ((not name) or (name not in library.keys())):
                print('Can not give book. There is no book like this in this system.')
            elif ((name in given.keys()) and (name not in not_given.keys())):
                print('Can not give book. Someone has already taken it.')
            else:
                if ((name not in given.keys()) and (name in not_given.keys())):
                    new_list = not_given[name]
                    new_list.append(param[1])
                    given[name] = new_list
                    not_given.pop(name)
                    print('{} has given with no problem.'.format(name))


def returnBook():
    param = input("\"book's name\" / \"book's number\"\n")
    if (not param):
        print('Can not return book(s). Missing parameter(s).')
    else:
        if (param.isdigit()):
            name = findNumber(library, param)
            if (name not in library.keys()):
                print('Can not return book. There is no book like this in this system.')
            else:
                if ((name in not_given.keys()) and (name not in given.keys())):
                    print('Can not return book. It has not been taken by anyone.')
                elif ((name in given.keys()) and (name not in not_given.keys())):
                    new_list = given[name][:-1]
                    not_given[name] = new_list
                    given.pop(name)
                    print('{} has been returned.'.format(name))
        elif (param.isdigit() == False):
            if (param not in library.keys()):
                print('Can not return book. There is no book like this in this system.')
            else:
                if ((param in not_given.keys()) and (param not in given.keys())):
                    print('Can not return book. It has not been taken by anyone.')
                elif ((param in given.keys()) and (param not in not_given.keys())):
                    new_list = given[param][:-1]
                    not_given[param] = new_list
                    given.pop(param)
                    print('{} has been returned.'.format(param))


def findBook():
    param = input("\"book's name\" / \"book's number\"\n")
    if (not param):
        print('Can not find book. Missing parameter(s).')
    else:
        if (param.isdigit() == False):
            if (param not in library.keys()):
                print('Can not find book. There is no book like this in this system.')
            elif (param in library.keys()):
                if (param in given.keys() and param not in not_given.keys()):
                    takenity = "book has taken"
                elif (param in not_given.keys() and param not in given.keys()):
                    takenity = "book has not taken"
                print('{} {} {} {} {} {}'.format(
                    takenity, library[param][0], library[param][1], library[param][2], library[param][3], library[param][4]))
        elif (param.isdigit() == True):
            param2 = findNumber(library, param)
            param = param2
            if (param not in library.keys()):
                print('Can not find book. There is no book like this in this system.')
            elif (param in library.keys()):
                if (param in given.keys() and param not in not_given.keys()):
                    takenity = "book has taken"
                elif (param in not_given.keys() and param not in given.keys()):
                    takenity = "book has not taken"
                print('{} {} {} {} {} {}'.format(
                    takenity, library[param][0], library[param][1], library[param][2], library[param][3], library[param][4]))


def findAuth(dict, n):
    for key in dict:
        if n in dict[key][4]:
            return key
    return None


def findNumber(dict, n):
    for key in dict:
        if n in dict[key][1]:
            return key
    return None


def listAuthorBook():
    param = input("\"author\'s name\"\n")
    if (not param):
        print('Can not list book(s). Missing parameter(s).')
    else:
        name = findAuth(library, param)
        if (not name):
            print('There are no books by this author in this system.')
        else:
            sorted_library = sorted(library, key=lambda k: library[k][1])
            for key in sorted_library:
                if (library[key][4] == param):
                    print(key, library[key][1])


def listBook():
    if (not library):
        print('There are no books in the system.')
    else:
        sorted_library = sorted(library, key=lambda k: library[k][1])
        for key in sorted_library:
            print(key, library[key][1])


def listTakenBook():
    if (not given):
        print('No one has taken books :(')
    else:
        sorted_library = sorted(given, key=lambda k: given[k][1])
        for key in sorted_library:
            print(given[key][0], given[key][1], given[key][6])


def checkSameYear(n):
    for i in library.keys():
        if (n != library[i][5]):
            return True
    return False


def listYear():
    inp = input("\"year\", \"before\" / \"after\"\n")
    params = inp.split(',')
    stripper(params)
    valid = ['before', 'after']
    if (len(params) != 2):
        print('Can not list book(s). Missing parameter(s).')
    elif (params[0].isdigit() == False) or (params[1] not in valid):
        print('Can not list book(s). Improper input.')
    elif ((not library) or checkSameYear(params[0]) == False):
        print('There are no books that is published {} {} in the system.'.format(
            params[1], params[0]))
    elif ((params[0].isdigit() == True) and (params[1].isdigit() == False and (params[1] == 'before' or params[1] == 'after')) and (len(params) == 2)):
        myBooks = {}
        if (params[1] == 'before'):
            for i in library.keys():
                if (int(params[0]) > int(library[i][5])):
                    myBooks[i] = library[i]
        elif (params[1] == 'after'):
            for i in library.keys():
                if (int(params[0]) < int(library[i][5])):
                    myBooks[i] = library[i]
        if (not myBooks):
            print('There are no books that is published {} {} in the system.'.format(
                params[1], params[0]))
        else:
            sorted_library = sorted(myBooks, key=lambda k: myBooks[k][1])
            for key in sorted_library:
                print(myBooks[key][0], myBooks[key][1])


def help():
    print('add book \t | -a | \t adds a new book to the system.')
    print('find book \t | -f | \t this command finds a book at the system.')
    print('list an author\'s books \t | -la | \t finds the books of an author which are in the system.')
    print('take book \t | -t | \t give a book to someone')
    print('return book \t | -t | \t returns a book which have taken by someone')
    print('list books \t | -l | \t lists every book in the system')
    print('list taken books \t | -lt | \t lists every taken book in the system')
    print('list books before/after year \t | -ly | \t lists every book in the system with given dates')
    print('help \t | -h | \t prints all commands and their descriptions')
    print('quit \t | -q | \t quits program')
    print('')


while (1):
    print('What would you want to do? (Write help for command list)')
    command = input()
    if (command == '-a' or command == 'add book'):
        addBook()
    elif (command == '-f' or command == 'find book'):
        findBook()
    elif (command == '-t' or command == 'take book'):
        takeBook()
    elif (command == '-r' or command == 'return book'):
        returnBook()
    elif (command == '-la' or command == 'list an author\'s books'):
        listAuthorBook()
    elif (command == '-l' or command == 'list books'):
        listBook()
    elif (command == '-lt' or command == 'list taken books'):
        listTakenBook()
    elif (command == '-ly' or command == 'list books before/after year'):
        listYear()
    elif (command == '-h' or command == 'help'):
        help()
    elif (command == '-q' or command == 'quit'):
        print('See you later :)')
        break
    elif (command == ''):
        pass
    elif (command == '-bb'):
        books()
    else:
        print('You have entered a command that does not exist. Write \'help\' to get to know commands.')
