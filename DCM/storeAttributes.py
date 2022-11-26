import sqlite3
# database CRUD methods and initialize sql


def createDB():  # create DB will create the database if it is not there otherwise will not do anything
    # connect to the database(creates it if not there)
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()  # cursor for executions
    try:
        # makes text file parameter.db creates if doesnt exist with schema user is pk for indentifying
        curs.execute('''CREATE TABLE userParams(
            USER text PRIMARY KEY NOT NULL, 
            LRL real,
            URL real,
            AAMP real,
            APW real,
            VAMP real,
            VPW real,
            VRP real,
            ARP real,
            MSR real, 
            Asens real,
            Vsens real,
            PVARP real,
            ActivityThresh real,
            Rxtime real,
            responseFactor real,
            recovTime real
         )''')  # docstring comment for multiple lines
        dbConnection.commit()  # close transaction
        curs.close()  # closes db
    except:
        print("already created parameter db\n")


def updateUser(username):  # creates new user with null parameter values
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    curs.execute('INSERT INTO userParams VALUES (:user,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)', {
                 'user': username})  # sql insertion with dictionary to insert variable
    # data = curs.execute('SELECT * From userParams')
    # print('create \n')
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


def paramDelete(username):  # deletes user
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()  # deletes row user matches username
    curs.execute('DELETE from userParams WHERE USER = :user',
                 {'user': username})
    # data = curs.execute('SELECT * From userParams')
    # print("delete \n") TESTING
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


# sets the parameters in the database based on the mode it is passed
def setParams(username, pChange, mode):
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    if (mode == "AOO"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3]})
    elif (mode == "VOO"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3]})
    elif (mode == "VOOR"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw, MSR= :msr, ActivityThresh= :activitythresh, Rxtime= :rxtime,responseFactor= :responsefactor, recovTime= :recovtime  WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3], 'msr': pChange[4], 'activitythresh': pChange[5], 'rxtime': pChange[6], 'responsefactor': pChange[7], 'recovtime': pChange[8]})
    elif (mode == "AOOR"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw, MSR= :msr, ActivityThresh= :activitythresh, Rxtime= :rxtime,responseFactor= :responsefactor, recovTime= :recovtime  WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3], 'msr': pChange[4], 'activitythresh': pChange[5], 'rxtime': pChange[6], 'responsefactor': pChange[7], 'recovtime': pChange[8]})
    elif (mode == "AAIR"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw, ARP= :arp, MSR= :msr, Asens= :asens, PVARP= :pvarp, ActivityThresh= :activitythresh, Rxtime= :rxtime,responseFactor= :responsefactor, recovTime= :recovtime  WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3], 'arp': pChange[4], 'msr': pChange[5], 'asens': pChange[6], 'pvarp': pChange[7], 'activitythresh': pChange[8], 'rxtime': pChange[9], 'responsefactor': pChange[10], 'recovtime': pChange[11]})
    elif (mode == "VVIR"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw, VRP= :vrp, MSR= :msr, Vsens= :vsens, ActivityThresh= :activitythresh, Rxtime= :rxtime,responseFactor= :responsefactor, recovTime= :recovtime  WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3], 'vrp': pChange[4], 'msr': pChange[5], 'vsens': pChange[6], 'activitythresh': pChange[7], 'rxtime': pChange[8], 'responsefactor': pChange[9], 'recovtime': pChange[10]})
    elif (mode == "AAI"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw, ARP= :arp, Asens= :asens, PVARP= :pvarp  WHERE USER= :user', {
            'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3], 'arp': pChange[4], 'asens': pChange[5], 'pvarp': pChange[6]})
    elif (mode == "VVI"):  # finds user and updates the specific parameters with order given by frontend
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw, VRP= :vrp, Vsens= :vsens WHERE USER= :user', {
            'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3], 'vrp': pChange[4], 'vsens': pChange[5]})
    else:
        print('mode doesnt exist')
    # data = curs.execute('SELECT * From userParams')
    # print("setting \n")  # TESTING
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


def getParams(username, mode):  # gets the parameters and returns list of values based on mode
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    params = []
    if (mode == "AOO"):  # gets specific parameters based on mode selected and username from query
        params = curs.execute('SELECT LRL,URL,AAMP,APW FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VOO"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,VAMP,VPW FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "AOOR"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,AAMP,APW,MSR,ActivityThresh,Rxtime,responseFactor,recovTime FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "AAIR"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,AAMP,APW,ARP,MSR,Asens,PVARP,ActivityThresh,Rxtime,responseFactor,recovTime FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VOOR"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,VAMP,VPW,MSR,ActivityThresh,Rxtime,responseFactor,recovTime FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VVIR"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,VAMP,VPW,VRP,MSR,Vsens,ActivityThresh,Rxtime,responseFactor,recovTime FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "AAI"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,AAMP,APW,ARP,Asens,PVARP FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VVI"):  # gets specific parameters based on mode selected and username
        params = curs.execute('SELECT LRL,URL,VAMP,VPW,VRP,Vsens FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "checkConn"):  # for checking connection
        params = curs.execute('SELECT LRL,AAMP,APW,ASens,ARP,VAMP,VPW,Vsens,VRP,Rxtime,recovTime FROM userParams WHERE USER= :user', {
            'user': username})
    else:
        print('mode doesnt exist')
        return []

    magic = params.fetchone()  # stack pops a tuple of the values of the query
    # empty list to be appended and returned values of magic (values of qry)
    paramsRow = []
    if (magic != None):
        for element in magic:
            paramsRow.append(element)
        curs.close()
        return paramsRow
    else:  # if query returns nothing returns None
        curs.close()
        print("empty")
        return None


# testing
# createDB()
# updateUser('test')
# setParams('bobby', [1, 2, 3, 4, 5], 'AOO')
# hi = getParams('test', 'AOO')
# print("this is what gets returned")
# print(hi)

# paramDelete('bobby')
