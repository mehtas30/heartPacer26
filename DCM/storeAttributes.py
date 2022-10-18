import sqlite3


def createDB():
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    try:
        # makes text file parameter.db creates if doesnt exist
        curs.execute('''CREATE TABLE userParams(
            USER text PRIMARY KEY NOT NULL,
            LRL real,
            URL real,
            AAMP real,
            APW real,
            VAMP real,
            VPW real,
            VRP real,
            ARP real
         )''')  # docstring comment for multiple lines
        dbConnection.commit()
        curs.close()
    except:
        print("already created parameter db\n")


def updateUser(username):
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    curs.execute('INSERT INTO userParams VALUES (:user,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)', {
                 'user': username})
    # data = curs.execute('SELECT * From userParams')
    # print('create \n')
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


def paramDelete(username):
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    curs.execute('DELETE from userParams WHERE USER = :user',
                 {'user': username})
    # data = curs.execute('SELECT * From userParams')
    # print("delete \n") TESTING
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


def setParams(username, pChange, mode):
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    if (mode == "AOO"):
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3]})
    elif (mode == "VOO"):
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw WHERE USER= :user', {
                     'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3]})
    elif (mode == "AAI"):
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, AAMP= :aamp, APW= :apw, ARP= :arp WHERE USER= :user', {
            'user': username, 'lrl': pChange[0], 'url': pChange[1], 'aamp': pChange[2], 'apw': pChange[3], 'arp': pChange[4]})
    elif (mode == "VVI"):
        curs.execute('UPDATE userParams set LRL= :lrl, URL= :url, VAMP= :vamp, VPW= :vpw, VRP= :vrp WHERE USER= :user', {
            'user': username, 'lrl': pChange[0], 'url': pChange[1], 'vamp': pChange[2], 'vpw': pChange[3], 'vrp': pChange[4]})
    else:
        print('mode doesnt exist')
    # data = curs.execute('SELECT * From userParams')
    # print("setting \n")  # TESTING
    # print(data.fetchall())  # testing
    dbConnection.commit()
    curs.close()


def getParams(username, mode):
    dbConnection = sqlite3.connect('parameter.db')
    curs = dbConnection.cursor()
    params = []
    if (mode == "AOO"):
        params = curs.execute('SELECT LRL,URL,AAMP,APW FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VOO"):
        params = curs.execute('SELECT LRL,URL,VAMP,VPW FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "AAI"):
        params = curs.execute('SELECT LRL,URL,AAMP,APW,ARP FROM userParams WHERE USER= :user', {
            'user': username})
    elif (mode == "VVI"):
        params = curs.execute('SELECT LRL,URL,VAMP,VPW,VRP FROM userParams WHERE USER= :user', {
            'user': username})
    else:
        print('mode doesnt exist')
        return []

    # print(params.fetchone())
    magic = params.fetchone()  # stack pop
    paramsRow = []
    if (magic != None):
        print("entered")
        for element in magic:
            paramsRow.append(element)
        curs.close()
        return paramsRow
    else:
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

# class AOOClass:
#     def __init__(self, user):
#         self.param = []
#         self.user = user

#     def getParam(self):
#         AOOTxt = open("AOO", "a+")
#         AOOLines = AOOTxt.readlines()
#         AOOLines = map(lambda x: x.strip(), AOOLines)
#         if (AOOLines == []):
#             return []
#         AOOTxt.close()
