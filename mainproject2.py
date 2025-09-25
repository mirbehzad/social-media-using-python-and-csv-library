import csv

class User:
    def __init__(self,name,lastname,year,month,day,gender,city,username,password):


        #Getting a correct name and lastname:

        self.name = name
        self.lastname = lastname
        with open('names.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)
            if [self.name,self.lastname] not in templst:
                with open('names.csv','a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.name,self.lastname])

        #Getting a correct year,month and day:

        self.year = year
        self.month = month
        self.day = day
        with open('dates.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)
            if [self.name,':' , self.year , self.month ,  self.day] not in templst:
                with open('dates.csv','a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.name,':' , self.year , self.month ,  self.day])

        #Getting a correct gender:

        self.gender = gender
        with open('genders.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)
            if [self.name,':',self.gender] not in templst:
                with open('genders.csv','a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.name,':',self.gender])

        #Getting a city:

        self.city = city
        with open('citis.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)
            if ["city of ",self.name,':',self.city] not in templst:
                with open('citis.csv','a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow(["city of ",self.name,':',self.city])

        #Getting correct username and password:
        self.username = username
        self.__password = password
        with open('usernames_and_passwords.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)
            if [self.username,self.__password] not in templst:
                with open('usernames_and_passwords.csv','a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.username,self.__password])
                with open('usernames.csv', 'a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.username])
                print("Account created!")

    #sign up function



    #login function:
    def login(self):

        username = input("Username: ")
        password = input("Password: ")

        with open('usernames_and_passwords.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            lst = []
            for line in data:
                lst.append(line)

            for i in lst:
                if [f'{username}', f'{password}'] in lst:
                    print("successfully loged in!")
                    with open('usernames.csv','r') as csvfile:
                        data = csv.reader(csvfile)
                        for line in data:
                            if line == [username]:
                                l = data.line_num
                                self.username = username
                                break
                    with open('names.csv', 'r') as csvfile:
                        data = csv.reader(csvfile)
                        for line in data:
                            if data.line_num == l:
                                self.name = line[0]
                                self.lastname = line[1]
                                break
                    with open('dates.csv','r') as csvfile:
                        data = csv.reader(csvfile)
                        for line in data:
                            if data.line_num == l:
                                self.year = line[2]
                                self.month = line[3]
                                self.day = line[4]
                                break
                    with open('genders.csv','r') as csvfile:
                        data = csv.reader(csvfile)
                        for line in data:
                            if data.line_num == l and line != []:
                                self.gender = line[2]
                                break
                    with open('citis.csv','r') as csvfile:
                        data = csv.reader(csvfile)
                        for line in data:
                            if data.line_num == l:
                                self.city = line[3]
                                break
                        break

                else:
                    choose = input('username or password is incorrect ! \n if you want to try again press [t] if you '
                                   'want to create account press[c]: ')
                    lst.clear()
                    while choose != 'c' and choose != 't':
                        choose = input('Please enter [c] or [t]: \n if you want to try again press [t] if you '
                                   'want to create account press[c]: ')
                    if choose == 't':
                        self.login()
                        break
                    else:
                        sign_up()
                        break



    def showPeople(self):
        with open('usernames.csv' , 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            for line in data:
                if line != []:
                    print(line)

    def addFriend(self):
        fusername = input("Please enter your friend's username: ")
        with open('usernames.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            templst = []
            for line in data:
                templst.append(line)

            with open('friends.csv', 'r') as csvfile:
                data = csv.reader(csvfile)
                tempflst = []
                for line in data:
                    tempflst.append(line)
            if [f'{fusername}'] in templst and [f'{self.username}', f'{fusername}'] not in tempflst:
                with open('friendRequest.csv', 'a') as csvfile:
                    data = csv.writer(csvfile)
                    data.writerow([self.username, 'sent a friend request to', fusername])
                print("request sent to",fusername)
            else:
                print("this username does not exist or it's already your friend!")

    def show_requests(self):
        with open('friendRequest.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            for line in data:
                if line != []:
                    if line[2] == self.username:
                        print(line)

    def accept_request(self):
        fusername = input('Please enter your friend username: ')
        with open('friendRequest.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            templst = []
            for line in data:
                templst.append(line)
        if [fusername, 'sent a friend request to', self.username] in templst:
            print("You accepted", fusername, "'s request!")
            with open('friends.csv', 'a') as csvfile:
                data = csv.writer(csvfile)
                data.writerow([self.username, fusername])
        else:
            print("your friend's username does not exict!")

    def reject_request(self):
        fusername = input('Please enterthe username you want to reject: ')
        with open('friendRequest.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            templst = []
            for line in data:
                templst.append(line)
        if [fusername, 'sent a friend request to', self.username] in templst:
            print("You rejected", fusername, "'s request!")
        else:
            print("friend's name does not exict!")

    def sendMessage(self):
        fusername = input("Please enter your friend's username: ")
        with open('friends.csv','r') as csvfile:
            data = csv.reader(csvfile)
            templst = []
            for line in data:
                templst.append(line)

            if [self.username,fusername] in templst or [fusername,self.username] in templst:
                message = input("Please enter yor message: (to exit enter 'exit':) ")
                while message != 'exit':
                    with open("messages.csv", "a", newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([self.username, fusername, message])
                    print("message sent to",fusername)
                    message = input("Please enter yor message: (to exit enter 'exit':) ")

            else:
                print(f'you are not friend with {fusername}!')
    def show_messages(self):
        with open('messages.csv','r') as csvfile:
            data = csv.reader(csvfile)
            data. __next__()
            for line in data:
                if line != [] and line[1] == self.username:
                    print(line)


class Admin(User):
    def Ashow_messages(self):
        with open('messages.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            for line in data:
                if line != [] :
                    print(line)


    def Ashow_friend(self):
        with open('friends.csv', 'r') as csvfile:
            data = csv.reader(csvfile)
            data.__next__()
            for line in data:
                if line != []:
                    print(line)


def sign_up():
    # name input:
    name = input("Please enter your firstname: ")
    while name.isalpha() == False:
        name = input("Please enter a correct name: ")

    # lastname input:
    lastname = input("Please enter your lastname: ")
    while lastname.isalpha() == False:
        lastname = input("Please enter a correct lastname: ")

    # Date inputs:
    year = input("Please enter your birth year: ")
    month = input("Please enter your birth month: ")
    day = input("Please enter your birth day: ")
    while year.isdigit() == False or month.isdigit() == False or day.isdigit() == False:
        year = input("Please enter a correct birth year: ")
        month = input("Please enter a correct birth month: ")
        day = input("Please enter a correct birthday: ")
    while (int(year) < 1300 or int(year) > 1500) or (int(month) < 0 or int(month) > 13) or (
            int(day) < 0 or int(day) > 32):
        year = input("Please enter a correct birth year: ")
        month = input("Please enter a correct birth month: ")
        day = input("Please enter a correct birthday: ")

    # Gender input:
    gender = input("Please enter you gender[male] or [female]: ")
    while gender != 'male' and gender != 'female':
        gender = input("Please enter a correct gender: ")

    # City input:
    city = input("Please enter your city: ")
    while city.isalpha() == False:
        city = input("Please enter a correct city: ")

    # Getting username and password:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with open('usernames_and_passwords.csv', 'r') as csvfile:
        for line in csvfile:
            while username in line:
                username = input("This username is in use try another one: ")
    while password.isdigit() or password.isalpha():
        password = input("Please enter a stronger password: ")
        break
    user1 = User(name, lastname, year, month, day, gender, city, username, password)
    user1.login()
def Asign_up():
    # name input:
    name = input("Please enter your firstname: ")
    while name.isalpha() == False:
        name = input("Please enter a correct name: ")

    # lastname input:
    lastname = input("Please enter your lastname: ")
    while lastname.isalpha() == False:
        lastname = input("Please enter a correct lastname: ")

    # Date inputs:
    year = input("Please enter your birth year: ")
    month = input("Please enter your birth month: ")
    day = input("Please enter your birth day: ")
    while year.isdigit() == False or month.isdigit() == False or day.isdigit() == False:
        year = input("Please enter a correct birth year: ")
        month = input("Please enter a correct birth month: ")
        day = input("Please enter a correct birthday: ")
    while (int(year) < 1300 or int(year) > 1500) or (int(month) < 0 or int(month) > 13) or (
            int(day) < 0 or int(day) > 32):
        year = input("Please enter a correct birth year: ")
        month = input("Please enter a correct birth month: ")
        day = input("Please enter a correct birthday: ")

    # Gender input:
    gender = input("Please enter you gender[male] or [female]: ")
    while gender != 'male' and gender != 'female':
        gender = input("Please enter a correct gender: ")

    # City input:
    city = input("Please enter your city: ")
    while city.isalpha() == False:
        city = input("Please enter a correct city: ")

    # Getting username and password:
    username = input("Please enter you username: ")
    password = input("Please enter your password: ")
    with open('usernames_and_passwords.csv', 'r') as csvfile:
        for line in csvfile:
            while username in line:
                username = input("This username is in use try another one: ")
    while password.isdigit() or password.isalpha():
        password = input("Please enter a stronger password: ")
        break
    user1 = Admin(name, lastname, year, month, day, gender, city, username, password)
    user1.login()

# menu

print("Welcome to MB's social network :))")
print("1-sign_up")
print("2-login")
print("3-exit")
print("#########################")

x = input("please enter a number (1 or 2 or 3 ):")
while True:
    if x != "1" and x != "2" and x !="3":
        x = input("error,please enter a number ( just 1 or 2 or 3 ):")
    else:
        if x == "1":
            print("1-sign up as user")
            print("2-sign up as admin")
            print("3-exit")
            print("#########################")

            n = input("Please enter a number (1 or 2 or 3): ")
            while n != '1' and n != '2' and n!='3':
                n = input("Please enter a number (1 or 2 or 3): ")
            if n == '1':
                sign_up()
                break
            elif n == '2':
                Asign_up()
                break
            else:
                break

        elif x == "2":
            print("1-login as a user")
            print("2-login as an admin")
            print("3-exit")
            print("#########################")

            m = input("Please enter a number(1 or 2 or 3): ")
            while m != '1' and m != '2' and m != '3':
                m = input("Please enter a number(1 or 2 or 3): ")
            if m == '1':
                user1 = User('behzad', 'shahriary', 1383, 6, 2, 'male', 'qom', 'behzadiniho', 'Mafb1383')
                user1.login()
                print("1-addFriend")
                print("2-sendMessage")
                print("3-showFriendRequests")
                print("4-exit")
                print("#########################")

                y=input("enter a number (1 or 2 or 3 or 4):")

                while y!= "1" and y != "2" and y!="3" and y != '4':

                    y = input("error,enter a number ( just 1 or 2 or 3 or 4):")

                if y=="1":
                    user1.showPeople()
                    user1.addFriend()
                    break

                elif y=="2":
                    user1.sendMessage()
                    user1.sendMessage()
                    break
                elif y == "3":
                    user1.show_requests()
                    print("1- accept request")
                    print("2- reject request")
                    print("3- exit")
                    print("#########################")

                    k = input("enter a number ( just 1 or 2 or 3) : ")
                    while k != '1' and k != '2' and k != '3':
                        k = input("enter a number ( just 1 or 2 or 3) : ")
                    if k == '1':
                        user1.accept_request()
                    elif k == '2':
                        user1.reject_request()
                    else:
                        break

                    break
                else:
                    break

            elif m == '2':
                user1 = Admin('behzad', 'shahriary', 1383, 6, 2, 'male', 'qom', 'behzadiniho', 'Mafb1383')
                user1.login()
                print("1-addFriend")
                print("2-sendMessage")
                print("3-showFriendRequests")
                print("4-showAllMessages")
                print("5-showAllFriends")
                print("6-exit")
                print("#########################")
                y = input("enter a number (1 or 2 or 3 or 4 or 5 or 6):")

                while y != "1" and y != "2" and y != "3" and y != '4' and y != '5' and y != '6':
                    y = input("error,enter a number ( just 1 or 2 or 3 or 4 or or 5 or 6):")

                if y == "1":
                    user1.showPeople()
                    user1.addFriend()
                    break

                elif y == "2":
                    user1.sendMessage()
                    user1.sendMessage()
                    break
                elif y == "3":
                    user1.show_requests()
                    print("1- accept request")
                    print("2- reject request")
                    print("3- exit")
                    print("#########################")

                    k = input("enter a number ( just 1 or 2 or 3) : ")
                    while k != '1' and k != '2' and k != '3':
                        k = input("enter a number ( just 1 or 2 or 3) : ")
                    if k == '1':
                        user1.accept_request()
                    elif k == '2':
                        user1.reject_request()
                    else:
                        break

                elif y=="4":
                    user1.Ashow_messages()
                    break
                elif y=="5":
                    user1.Ashow_friend()
                    break

                else:
                    break

            else:
                break



        else:
            break











