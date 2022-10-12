def counter():
    database = open("Database", "r") #open and read the database text file
    counts = 0 #create a variable counts and set the intial value to 0
    line = database.readlines() #create a variable line and set it to read the lines in the database text file
    for i in range(len(line)): #for loop for the length of line
        if line == "": #if line is equal to an empty string
            break #break the for loop
        counts += 1 #add 1 to the variable counts
    database.close() #close the database
    return counts #return the variable counts


def signup():
    database = open("Database", "r") #open and read the database text file
    count = counter() #create a variable count and set it equal to counter ()
    if count == 10: #if the count is equal to 10
        print("Maximum accounts reached, please login into a existing account or delete an account") #let the user know the maximum amount of accounts have been reached (10)
        select() #give the user another attempt to choose what to do either signup, login or delete
    else: #if there is less than 10 users created let the user signup and create a new account
        username = input("Create Username:") #create a username for the new account
        password = input("Create Password:") #create a password for the new account
        confirm_password = input("Confirm Password") #double checks the password, confirms the password
        x = [] #create an empty array x
        y = [] #create an empty array y
        for i in database: #for loop for every i in database
            a, b = i.split(", ") #splits the inputs for username and password by a comma
            b = b.strip() #take out all the extra space inputs
            x.append(a) #add the string into the array
            y.append(b) #add the string into the array
        if password != confirm_password: #if the passowrd doesn't equal confirm password
            print("Passwords don't match, please try again") #tell the user to try again as the passwords entered don't match each other
            signup() #give the user another attempt to signup
        else: #if the passwords match then
            if len(password) < 4: #make sure the password is longer than 4 characters
                print("Password to short, please have more than 4 characters") #if the password is not longer than 4 charecters then tell the user the passwords to short
                signup() #give the user another attempt to signup
            elif username in x: #if the username is already in the array x
                print("Username already exists, please sign in or create a new username") #tell the user that the username already exists in the database
                select() #give the user another attempt to choose what to do either signup, login or delete
            elif username == password: #if the password and username are the same
                print("Password and Username can not be the same") #tell the user that the password and username can't be the same
                signup() #give the user another attempt to signup
            else: #if everything passes then
                database = open("Database", "a") #open up the databse text file
                database.write(username + ", " + password + "\n") #write the new username and passwords created
                database.close() #close the database
                print("Successfully created an account for", username, "please login") #tell the user that the new account is succesfully created
                login() #give the user a chance to login


def login():
    database = open("Database", "r") #open and read the database text file
    username = input("Enter your Username:") #ask the user to enter the username they want to login into
    password = input("Enter your Password:") #ask the user to enter the password for the account they want to login to
    if not len(password or username) < 1: #if the number of chartecters entered for username or password is not less then 1 then
        x = []  #create an empty array x
        y = []  #create an empty array y
        for i in database:  #for loop for every i in database
            a, b = i.split(", ")  #splits the inputs for username and password by a comma
            b = b.strip()  #take out all the extra space inputs
            x.append(a)  #add the string into the array
            y.append(b)  #add the string into the array
            data = dict(zip(x, y)) #create a new variable called data and pass the arrays
        try:
            if data[username]: #if username is in data
                try:
                    if password == data[username]: #check if the password and the username are correct if they are then
                        print("Login successful welcome", username) #let the user know that they've succesfully logged in
                    else: #if the password and username is not correct then
                        print("Password or username is incorrect, please try again")  #let the user know that the password entered or the username is inccorect and tell them to try again
                        login() #run login
                except:
                    print("Password or username is incorrect, please try again")#let the user know that the password entered or the username is inccorect and tell them to try again
                    login() #run login
            else: #if the username or password doesn't exist then
                print("Username or password does not exist, please create an account or sign in using an existing account") #let the user know that the username or password does not existm and they shouuld either create an account or sign in using an existing account
                select() #run select
        except:
            print("Username or password does not exist, please create an account or sign in using an existing account") #let the user know that the username or password does not existm and they shouuld either create an account or sign in using an existing account
            select() #run select
    else: #if the user does not input an option
        print("Please choose one of the following options") #let the user know that they need to choose one of the options listed
        login() #run login
    database.close() #close database text file


def delete():
    database = open("Database", "r")  # open and read the database text file
    username = input("Enter your Username:")  # ask the user to enter the username they want to delete
    password = input("Enter your Password:")  # confirm the password of the username they want to delete
    line = database.readlines()  # create a variable line and set it to read the lines in the database text file
    for i in range(len(line)):  # for i in the range of the length of line
        if (username + ", " + password + "\n") == line[i]:  # if the username and password entered is equal to line then
            line.remove(line[i])  # remove the line which will delete that account
            print("Successfully deleted", username,"please create a new account, or login")  # let the user name the account is deleted
            break
    database = open("Database", "w")  # open and write in the database text file
    for i in line:  # for i in line
        database.write(i)  # write it in the text file
    database.close()  # close the text file
    select()  # run select


def select():
    option = input("Login | Signup | Delete:") #asks user for what they want to do either login, signup, or delete an account
    if option == "Signup": #if user chooses signup
        signup() #run signup
    elif option == "Login": #if user chooses login
        login() #run login
    elif option == "Delete": #if user chooses delete
        delete() #run delete
    else:
        print("Please select an option") #if user doesn't seleect anything, tell them to select something
        select() #run select


select()
