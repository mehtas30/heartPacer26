connected = False
pmID = 341  # example pace maker ID from serial com- will store to db for next time
previousId = 431  # will get from database
if (pmID == previousId):
    different = False
else:
    different = True

# if connected change- reload gui with tk.after
