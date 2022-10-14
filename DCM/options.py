def counter():
    database = open("Database", "r")  # open and read the database text file
    counts = 0  # create a variable counts and set the intial value to 0
    # create a variable line and set it to read the lines in the database text file
    line = database.readlines()
    for i in range(len(line)):  # for loop for the length of line
        if line == "".strip():  # if line is equal to an empty string
            break  # break the for loop
        counts += 1  # add 1 to the variable counts
    database.close()  # close the database
    return counts  # return the variable counts


def signup(username, password, confirm_password):
    database = open("Database", "a")
    database.close()
    # incase database doesnt exist
    database = open("Database", "r")  # open and read the database text file
    count = counter()  # create a variable count and set it equal to counter ()
    if count == 10:  # if the count is equal to 10
        # let the user know the maximum amount of accounts have been reached (10)
        print("Maximum accounts reached, please login into a existing account or delete an account")
        return 0, "Maximum accounts reached, please login into a existing account or delete an account"
        # select()  # give the user another attempt to choose what to do either signup, login or delete
    else:  # if there is less than 10 users created let the user signup and create a new account
        # create a username for the new account
        # username = input("Create Username:")
        # # create a password for the new account
        # password = input("Create Password:")
        # # double checks the password, confirms the password
        # confirm_password = input("Confirm Password")
        x = []  # create an empty array x
        y = []  # create an empty array y
        for i in database:  # for loop for every i in database
            # splits the inputs for username and password by a comma
            if (i == ""):
                break
            else:
                a, b = i.split(", ")
                b = b.strip()  # take out all the extra space inputs
                x.append(a)  # add the string into the array
                y.append(b)  # add the string into the array
        if password != confirm_password:  # if the passowrd doesn't equal confirm password
            # tell the user to try again as the passwords entered don't match each other
            print("Passwords don't match, please try again")
            return 1, "Passwords don't match, please try again"
        else:  # if the passwords match then
            if len(password) < 4:  # make sure the password is longer than 4 characters
                # if the password is not longer than 4 charecters then tell the user the passwords to short
                print("Password to short, please have more than 4 characters")
                # signup()  # give the user another attempt to signup
                return 1, "Password to short, please have more than 4 characters"
            elif username.strip() == "":
                return 1, "Username cannot be blank"
            elif username in x:  # if the username is already in the array x
                # tell the user that the username already exists in the database
                print("Username already exists, please sign in or create a new username")
                # select()  # give the user another attempt to choose what to do either signup, login or delete
                return 0, "Username already exists, please sign in or create a new username"
            elif username.strip() == password.strip():  # if the password and username are the same
                # tell the user that the password and username can't be the same
                print("Password and Username can not be the same")
                # signup()  # give the user another attempt to signup
                return 1, "Password and Username can not be the same"
            else:  # if everything passes then
                # open up the databse text file
                database = open("Database", "a")
                # write the new username and passwords created
                database.write(username + ", " + password + "\n")
                database.close()  # close the database
                paraDb = open("ParamDb", 'a')
                paraDb.write("user: "+username+"\n")
                modes = ['AOO', 'VOO', 'AAI', 'VVI']
                for mode in modes:
                    paraDb.write(mode+": "+"\n")
                paraDb.close()
                # tell the user that the new account is succesfully created
                print("Successfully created an account for",
                      username, "please login")
                # login()  # give the user a chance to login
                return 2, "Successfully created an account! please login"


def login(username, password):
    returnArr = []
    database = open("Database", "a") #creates db if not there
    database.close()
    database = open("Database", "r")  # open and read the database text file
    # if the number of chartecters entered for username or password is not less then 1 then
    if not len(password or username) < 1:
        x = []  # create an empty array x
        y = []  # create an empty array y
        for i in database:  # for loop for every i in database
            # splits the inputs for username and password by a comma
            a, b = i.split(", ")
            b = b.strip()  # take out all the extra space inputs
            x.append(a)  # add the string into the array
            y.append(b)  # add the string into the array
            # create a new variable called data and pass the arrays
            data = dict(zip(x, y))
        try:
            if data[username]:  # if username is in data
                try:
                    # check if the password and the username are correct if they are then
                    if password == data[username]:
                        # let the user know that they've succesfully logged in
                        # print("Login successful welcome", username)
                        returnArr = [2, "Login successful welcome"]
                    else:  # if the password and username is not correct then
                        # let the user know that the password entered or the username is inccorect and tell them to try again
                        # print("Password or username is incorrect, please try again")
                        # login()  # run login
                        returnArr = [
                            0, "Password or username is incorrect, please try again"]
                except:
                    # let the user know that the password entered or the username is inccorect and tell them to try again
                    # print("Password or username is incorrect, please try again")
                    # login()  # run login
                    returnArr = [
                        0, "Password or username is incorrect, please try again"]
            else:  # if the username or password doesn't exist then
                # let the user know that the username or password does not existm and they shouuld either create an account or sign in using an existing account
                # print(
                #     "Username or password does not exist, please create an account or sign in using an existing account")
                # select()  # run select
                returnArr = [
                    1, "Username or password does not exist, please create an account or sign in using an existing account"]
        except:
            # let the user know that the username or password does not existm and they shouuld either create an account or sign in using an existing account
            #     "Username or password does not exist, please create an account or sign in using an existing account")
            # select()  # run select
            returnArr = [
                1, "Username or password does not exist, please create an account or sign in using an existing account"]
    else:  # if the user does not input an option
        # let the user know that they need to choose one of the options listed
        # print("Please choose one of the following options")
        # login()  # run login
        returnArr = [0, "please enter user and password"]
    database.close()  # close database text file
    return returnArr


def delete(username, password):
    database = open("Database", "a")
    database.close()
    database = open("Database", "r")  # open and read the database text file
    # create a variable line and set it to read the lines in the database text file
    confirm = ""
    line = database.readlines()
    for i in range(len(line)):  # for i in the range of the length of line
        # if the username and password entered is equal to line then
        if (username + ", " + password + "\n") == line[i]:
            # remove the line which will delete that account
            line.remove(line[i])
            # let the user name the account is deleted
            confirm = "Successfully deleted! please create a new account, or login"
            break
    # open and write in the database text file
    database = open("Database", "w")
    for i in line:  # for i in line
        database.write(i)  # write it in the text file
    database.close()  # close the text file
    if (confirm == ""):
        return "user account not found"
    else:
        return confirm


# def select():
#     # asks user for what they want to do either login, signup, or delete an account
#     option = input("Login | Signup | Delete:")
#     if option.casefold() == "Signup".casefold():  # if user chooses signup
#         signup()  # run signup
#     elif option.casefold() == "Login".casefold():  # if user chooses login
#         login()  # run login
#     elif option.casefold() == "Delete".casefold():  # if user chooses delete
#         delete()  # run delete
#     else:
#         # if user doesn't seleect anything, tell them to select something
#         print("Please select an option")
#         select()  # run select
