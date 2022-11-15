import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("******** Welcome to BookMYShow ********")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Movies To Info")
    print("2 - View Info")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            addMovieDetailsToInfo()
            break
        elif userChoice == '2':
            viewInfo()
            break

def addMovieDetailsToInfo():
    clear()
    print("ADD NEW MOVIES TO INFO")
    print("----------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add new movies to info")
    print()
    while True:
        userChoice = input("Choose an option: ")
        if userChoice in ['1']:
            break
    if userChoice == '1':
        print()
        while True:
            Movies = input("Enter the number of Details to be added: ")
            if Movies.isdigit():
                break
        movies = int(Movies)
        userMovies = {}
        for i in range(1, movies+1):
            while True:
                print()
                user_Movie = input("Description : ")
                if user_Movie != '':
                    break

            while True:
                user_Movie = input("Information : ")
                if user_Movie != '':
                    break
            userMovies.update({user_Movie: str(user_Movie)})

        addMovieDetailsToFile(userMovies, Info=False)
        returnToMainMenu("Entered details Have Been Added")


def viewInfo():
    clear()
    print("VIEW INFO")
    print("--------------")
    print()
    invMovies = getInvItems()
    print("MOVIES")
    print("-----")
    print()
    for movies in invMovies:
        print(f"{movies}: {invMovies[movies]}")

    print()
    print("Available Options:")
    print()
    print("1 - Edit Movie Info")
    print("2 - Delete Movie Info ")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            editMovieInfo()
            break
        elif userChoice == '2':
            deleteMovieInfo()
            break

def editMovieInfo():
    clear()
    print("EDIT MOVIE INFO")
    print("-------------------")
    print("Press (B) To Go Back")
    print()
    print("Available Options")
    print()
    print("1 - Edit Movie Description")
    print("2 - Edit Movie Information")
    print()
    while True:
        userChoice = input("Choose An Option: ").lower()
        if userChoice in ['1', '2', 'b']:
            break
    if userChoice == 'b':
        main()

    invMovies = getInvItems()
    if userChoice == '1':
        print()
        while True:
            MovieToChange = input("Enter The Name Of The Description To Edit: ")
            if MovieToChange in invMovies:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newMovieName = input("Enter The New Item Name: ")
            if newMovieName != '':
                break
        invMovies.update({newMovieName: invMovies[MovieToChange]})
        del invMovies[MovieToChange]

        addMovieDetailsToFile(invMovies, Info=True)
        returnToMainMenu("Details Has Been Changed")

    elif userChoice == '2':
        print()
        while True:
            MovieToChange = input("Enter The Name Of The Description To Edit: ")
            if MovieToChange in invMovies:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newInfoName = input("Enter The New Item Information: ")
            if newInfoName != '':
                break
        invMovies.update({MovieToChange: newInfoName})
        addMovieDetailsToFile(invMovies, Info=True)
        returnToMainMenu("Item Amount Has Been Changed")

def deleteMovieInfo():
    print("DELETE MOVIE INFO")
    print("---------------------")
    print()
    invMovies = getInvItems()
    while True:
        itemToDelete = input("Enter The Name Of The Item To Delete: ")
        if itemToDelete in invMovies:
            break
        else:
            print("That Item Does Not Exist")
            print()

    while True:
       confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item: ").lower()
       if confirmation in ['yes', 'no']:
           break
    if confirmation == 'yes':
        del invMovies[itemToDelete]
        addMovieDetailsToFile(invMovies, Info=True)
        returnToMainMenu("Item Has Been Deleted")
    else:
        main()

def addMovieDetailsToFile(userMovies: dict, Info: bool):
    if Info:
        f = open('userItems.txt', 'w')
        f.close()
        with open('userItems.txt', 'a') as file:
            for item in userMovies:
                file.write(f"{item}: {userMovies[item]}")
                file.write('\n')
        return
    invItems = getInvItems()
    for item in userMovies:
        # CHECK IF THE ITEM HAS ALREADY BEEN ADDED
        if item in invItems:
            invItems[item] += userMovies[item]
    with open('userItems.txt', 'a') as file:
        for item in invItems:
            file.write(f"{item}: {invItems[item]}")
            file.write('\n')

def getInvItems():
    invItems = {}
    with open('userItems.txt', 'r') as file:
        for line in file:
            line = line.replace('\n','').split(':')
            itemName, itemInfo = line[0], line[1].strip()
            invItems.update({itemName: str(itemInfo)})

    return invItems

def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower() if message != None else input("Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main()
            break


main()