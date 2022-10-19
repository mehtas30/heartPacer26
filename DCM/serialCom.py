connected = False  # initial value of connected- will change with serial com
pmID = 341  # example pace maker ID from serial com- will store to db for next time
previousId = 431  # will get from database
if (pmID == previousId):  # checks id of pacemaker and gives value to boolean different
    different = False
else:
    different = True

# if connected change- reload gui with tk.after
