print("Welcome to MB's social network :))")
print("1-sign up")
print("2-login")
x = input("please enter a number (1 or 2 ):")
while True:
    if x != "1" and x != "2":
        x = input("error,please enter just (1 or 2 ):")
    else:
        if x == "1":
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
        elif x == "2":
            user1.login()



















