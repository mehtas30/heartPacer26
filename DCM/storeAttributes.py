def readMethod(user, mode):
    params = []
    paramDb = open("ParamDb", 'r')
    lines = paramDb.readlines()
    for i in range(len(lines)):
        nameSplit = lines[i].split(":")
        name = nameSplit[1].strip()
        print(name+"ns1")
        if (name == user):
            print("first if done")
            modeFound = 0
            i += 1
            while (modeFound == 0):
                modeSplit = lines[i].split(":")
                modeSplit[0].strip()
                print(modeSplit)
                if (modeSplit[0] == mode):
                    print("found")
                    modeFound = 1
                else:
                    i += 1
            params = modeSplit[1].strip().split(",")
            print("params"+params[0]+" "+params[8])
    paramDb.close()
    return params
