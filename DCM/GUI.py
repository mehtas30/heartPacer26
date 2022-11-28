import enum
import tkinter as tk
from tkinter import messagebox
from tkinter.tix import COLUMN
from options import *
from storeAttributes import *
from serialCom import *
from Egram import *


BGCOLOR = "#800000"  # background color of gui-maroon
# Runs gui and controls program


class gui(tk.Tk):  # tk.TK is root
    # controller for pages
    # *args and **kwargs can receive multiple parameters kwargs is for named values
    def __init__(self, *args, **kwargs):
        # init for tkinter functionality (superclass)
        tk.Tk.__init__(self, *args, **kwargs)
        # shared parameters that can be used throughout all frames
        self.sharedUser = {"username": tk.StringVar(), "mode": tk.StringVar()}
        container = tk.Frame()  # container for frames
        # pack means place, expandable window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.pageInfo = {}  # empty dictionary for page name and object
        # sets properties of frame windows
        for page in (
            welcomeP,
            loginP,
            signupP,
            deleteP,
            afterLogin,
            modeP,
        ):
            pageName = page.__name__  # magic  method to get object name -pythons cool
            # parent as container for frame, with self as controller to use function in gui
            frame = page(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nesw")
            # pagename dictionary with frame objects
            self.pageInfo[pageName] = frame
        self.dispFrame("welcomeP")  # show welcome first

    def dispFrame(self, pageName):  # display frame based on name- creates instances
        page = self.pageInfo[pageName]
        page.tkraise()  # raises frame over the other frames to be visible


class welcomeP(tk.Frame):  # Frame is parent
    def __init__(self, parent, controller):  # init object as specified in gui
        # init frame to get tkinter frame properties
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = (
            controller  # controller to get access to gui variables/methods
        )
        self.controller.title("Heart Pacer 26")  # title on top of window
        # welcome label
        title = tk.Label(
            self,
            text="Welcome",
            fg="#F2BA49",
            bg=BGCOLOR,  # page title- different from window title
            justify="center",
            font="default, 25",
        )
        # title.place(x=400, y=100, anchor=CENTER)
        title.pack(pady=10, padx=300)  # place title at coordinates
        # buttons for option select on welcome screen
        loginButt = tk.Button(
            self,
            text="Login",
            width=20,
            height=2,
            command=lambda: controller.dispFrame("loginP"),
        )  # lamda is needed for controller arguments- calls next frame
        signButt = tk.Button(
            self,
            text="Signup",
            width=20,
            height=2,
            command=lambda: controller.dispFrame("signupP"),
        )
        deleteButt = tk.Button(
            self,
            text="Delete",
            width=20,
            height=2,
            command=lambda: controller.dispFrame("deleteP"),
        )
        # placement of buttons underneath each other
        loginButt.pack(pady=5)
        signButt.pack(pady=5)
        deleteButt.pack(pady=5)


class modeP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller
        # DoubleVar is needed for tk labels/entries to be able to take in variable as args and too pass to other frames
        LRLStringVar = tk.DoubleVar(self, 0.0)
        URLStringVar = tk.DoubleVar(self, 0.0)
        AampStringVar = tk.DoubleVar(self, 0.0)
        APWStringVar = tk.DoubleVar(self, 0.0)
        VampStringVar = tk.DoubleVar(self, 0.0)
        VPWStringVar = tk.DoubleVar(self, 0.0)
        ARPStringVar = tk.DoubleVar(self, 0.0)
        VRPStringVar = tk.DoubleVar(self, 0.0)
        MSRStringVar = tk.DoubleVar(self, 0.0)
        AsensStringVar = tk.DoubleVar(self, 0.0)
        VsensStringVar = tk.DoubleVar(self, 0.0)
        PVARPStringVar = tk.DoubleVar(self, 0.0)
        ActivityThreshStringVar = tk.DoubleVar(self, 0.0)
        RxtimeStringVar = tk.DoubleVar(self, 0.0)
        responseFactorStringVar = tk.DoubleVar(self, 0.0)
        recovTimeStringVar = tk.DoubleVar(self, 0.0)
        # to be set/displayed

        # displaying parameters by getting them from SQL db user/mode needed for qry
        def displayParam(userName, mode):
            # removes buttons to make room to display label without making a new frame
            readButt.grid_remove()
            setButt.grid_remove()
            if mode == "AOO":  # parameters get displayed based on mode
                # database function to get list of parameters
                parameterList = getParams(userName, mode)
                if parameterList == None:  # empty list case
                    parameterlabel.config(text="no parameters")
                else:
                    # Changes the text of the label from blank to display parameters
                    # Will already be in order from sql query
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n AAMP: "
                        + str(parameterList[2])
                        + "\n APW: "
                        + str(parameterList[3])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "":  # empty mode will change the label to be empty
                parameterlabel.config(text="")
            elif mode == "VOO":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n VAMP: "
                        + str(parameterList[2])
                        + "\n VPW: "
                        + str(parameterList[3])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "VVI":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n VAMP: "
                        + str(parameterList[2])
                        + "\n VPW: "
                        + str(parameterList[3])
                        + "\n VRP: "
                        + str(parameterList[4])
                        + "\n V Sensitivity: "
                        + str(parameterList[5])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "AAI":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    # get from text file
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n AAMP: "
                        + str(parameterList[2])
                        + "\n APW: "
                        + str(parameterList[3])
                        + "\n ARP: "
                        + str(parameterList[4])
                        + "\n A Sensitivity: "
                        + str(parameterList[5])
                        + "\n  PVARP: "
                        + str(parameterList[6])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "AOOR":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    # get from text file
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n AAMP: "
                        + str(parameterList[2])
                        + "\n APW: "
                        + str(parameterList[3])
                        + "\n MSR: "
                        + str(parameterList[4])
                        + "\n  Activity Threshold: "
                        + str(parameterList[5])
                        + "\n  Reaction Time: "
                        + str(parameterList[6])
                        + "\n  Response Factor: "
                        + str(parameterList[7])
                        + "\n  Recovery Time: "
                        + str(parameterList[8])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "VOOR":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    # get from db
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n VAMP: "
                        + str(parameterList[2])
                        + "\n VPW: "
                        + str(parameterList[3])
                        + "\n MSR: "
                        + str(parameterList[4])
                        + "\n  Activity Threshold: "
                        + str(parameterList[5])
                        + "\n  Reaction Time: "
                        + str(parameterList[6])
                        + "\n  Response Factor: "
                        + str(parameterList[7])
                        + "\n  Recovery Time: "
                        + str(parameterList[8])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "AAIR":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    # get from text file
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n AAMP: "
                        + str(parameterList[2])
                        + "\n APW: "
                        + str(parameterList[3])
                        + "\n ARP: "
                        + str(parameterList[4])
                        + "\n A Sensitivity: "
                        + str(parameterList[5])
                        + "\n  PVARP: "
                        + str(parameterList[6])
                        + "\n MSR: "
                        + str(parameterList[7])
                        + "\n  Reaction Time: "
                        + str(parameterList[8])
                        + "\n  Response Factor: "
                        + str(parameterList[9])
                        + "\n  Recovery Time: "
                        + str(parameterList[10])
                    )
                    parameterlabel.config(text=pLabelText)
            elif mode == "VVIR":  # same concept as AOO above
                parameterList = getParams(userName, mode)
                if parameterList == None:
                    parameterlabel.config(text="no parameters")
                else:
                    # get from text file
                    pLabelText = (
                        "LRL: "
                        + str(parameterList[0])
                        + "\n URL: "
                        + str(parameterList[1])
                        + "\n VAMP: "
                        + str(parameterList[2])
                        + "\n VPW: "
                        + str(parameterList[3])
                        + "\n VRP: "
                        + str(parameterList[4])
                        + "\n V Sensitivity: "
                        + str(parameterList[5])
                        + "\n MSR: "
                        + str(parameterList[7])
                        + "\n  Reaction Time: "
                        + str(parameterList[8])
                        + "\n  Response Factor: "
                        + str(parameterList[9])
                        + "\n  Recovery Time: "
                        + str(parameterList[10])
                    )
                    parameterlabel.config(text=pLabelText)
            else:  # incase something goes wrong and for testing
                parameterlabel.config(text="Mode does not exist yet")
            # places the label to be viewed
            parameterlabel.grid(row=2, column=1)

        def setParam(
            mode,
        ):  # sets the parameters with option given to user based on mode selected (ONLY FOR DISPLAY SUBMIT IS BELOW)
            readButt.grid_remove()  # removes button to make room for entry boxes
            setButt.grid_remove()

            if (
                mode == "AOO"
            ):  # Aoo mode will only give option to change aoo related parameters
                # changes entry variable to specific parameter variable
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[2].config(textvariable=AampStringVar)
                paramEntries[3].config(textvariable=APWStringVar)
                for i in range(4):  # places the instruction lables and entries
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)

            elif mode == "VOO":  # same as AOO
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[4].config(textvariable=VampStringVar)
                paramEntries[5].config(textvariable=VPWStringVar)
                for i in range(2):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[4].grid(row=3, column=0, pady=5)
                paramInstructions[5].grid(row=4, column=0, pady=5)
                paramEntries[4].grid(row=3, column=1, pady=5)
                paramEntries[5].grid(row=4, column=1, pady=5)

            elif mode == "AAI":  # same as AOO
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[2].config(textvariable=AampStringVar)
                paramEntries[3].config(textvariable=APWStringVar)
                paramEntries[7].config(textvariable=ARPStringVar)
                paramEntries[9].config(textvariable=AsensStringVar)
                paramEntries[11].config(textvariable=PVARPStringVar)
                for i in range(4):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[7].grid(row=5, column=0, pady=5)
                paramEntries[7].grid(row=5, column=1, pady=5)
                paramInstructions[9].grid(row=6, column=0, pady=5)
                paramEntries[9].grid(row=6, column=1, pady=5)
                paramInstructions[11].grid(row=7, column=0, pady=5)
                paramEntries[11].grid(row=7, column=1, pady=5)
            elif mode == "VVI":  # same as AOO
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[4].config(textvariable=VampStringVar)
                paramEntries[5].config(textvariable=VPWStringVar)
                paramEntries[6].config(textvariable=VRPStringVar)
                paramEntries[10].config(textvariable=VsensStringVar)
                for i in range(2):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[4].grid(row=3, column=0, pady=5)
                paramEntries[4].grid(row=3, column=1, pady=5)
                paramInstructions[5].grid(row=4, column=0, pady=5)
                paramEntries[5].grid(row=4, column=1, pady=5)
                paramInstructions[6].grid(row=5, column=0, pady=5)
                paramEntries[6].grid(row=5, column=1, pady=5)
                paramInstructions[10].grid(row=6, column=0, pady=5)
                paramEntries[10].grid(row=6, column=1, pady=5)
            elif mode == "AOOR":
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[2].config(textvariable=AampStringVar)
                paramEntries[3].config(textvariable=APWStringVar)
                paramEntries[8].config(textvariable=MSRStringVar)
                paramEntries[12].config(textvariable=ActivityThreshStringVar)
                paramEntries[13].config(textvariable=RxtimeStringVar)
                paramEntries[14].config(textvariable=responseFactorStringVar)
                paramEntries[15].config(textvariable=recovTimeStringVar)
                for i in range(4):  # places the instruction lables and entries
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[8].grid(row=5, column=0, pady=5)
                paramEntries[8].grid(row=5, column=1, pady=5)
                paramInstructions[12].grid(row=6, column=0, pady=5)
                paramEntries[12].grid(row=6, column=1, pady=5)
                paramInstructions[13].grid(row=7, column=0, pady=5)
                paramEntries[13].grid(row=7, column=1, pady=5)
                paramInstructions[14].grid(row=8, column=0, pady=5)
                paramEntries[14].grid(row=8, column=1, pady=5)
                paramInstructions[15].grid(row=9, column=0, pady=5)
                paramEntries[15].grid(row=9, column=1, pady=5)
            elif mode == "VOOR":
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[4].config(textvariable=VampStringVar)
                paramEntries[5].config(textvariable=VPWStringVar)
                paramEntries[8].config(textvariable=MSRStringVar)
                paramEntries[12].config(textvariable=ActivityThreshStringVar)
                paramEntries[13].config(textvariable=RxtimeStringVar)
                paramEntries[14].config(textvariable=responseFactorStringVar)
                paramEntries[15].config(textvariable=recovTimeStringVar)
                for i in range(2):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[4].grid(row=3, column=0, pady=5)
                paramInstructions[5].grid(row=4, column=0, pady=5)
                paramEntries[4].grid(row=3, column=1, pady=5)
                paramEntries[5].grid(row=4, column=1, pady=5)
                paramInstructions[8].grid(row=5, column=0, pady=5)
                paramEntries[8].grid(row=5, column=1, pady=5)
                paramInstructions[12].grid(row=6, column=0, pady=5)
                paramEntries[12].grid(row=6, column=1, pady=5)
                paramInstructions[13].grid(row=7, column=0, pady=5)
                paramEntries[13].grid(row=7, column=1, pady=5)
                paramInstructions[14].grid(row=8, column=0, pady=5)
                paramEntries[14].grid(row=8, column=1, pady=5)
                paramInstructions[15].grid(row=9, column=0, pady=5)
                paramEntries[15].grid(row=9, column=1, pady=5)
            elif mode == "VVIR":
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[4].config(textvariable=VampStringVar)
                paramEntries[5].config(textvariable=VPWStringVar)
                paramEntries[6].config(textvariable=VRPStringVar)
                paramEntries[10].config(textvariable=VsensStringVar)
                paramEntries[8].config(textvariable=MSRStringVar)
                paramEntries[12].config(textvariable=ActivityThreshStringVar)
                paramEntries[13].config(textvariable=RxtimeStringVar)
                paramEntries[14].config(textvariable=responseFactorStringVar)
                paramEntries[15].config(textvariable=recovTimeStringVar)
                for i in range(2):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[4].grid(row=3, column=0, pady=5)
                paramInstructions[5].grid(row=4, column=0, pady=5)
                paramEntries[4].grid(row=3, column=1, pady=5)
                paramEntries[5].grid(row=4, column=1, pady=5)
                paramInstructions[6].grid(row=5, column=0, pady=5)
                paramEntries[6].grid(row=5, column=1, pady=5)
                paramInstructions[10].grid(row=6, column=0, pady=5)
                paramEntries[10].grid(row=6, column=1, pady=5)
                paramInstructions[8].grid(row=7, column=0, pady=5)
                paramEntries[8].grid(row=7, column=1, pady=5)
                paramInstructions[12].grid(row=8, column=0, pady=5)
                paramEntries[12].grid(row=8, column=1, pady=5)
                paramInstructions[13].grid(row=9, column=0, pady=5)
                paramEntries[13].grid(row=9, column=1, pady=5)
                paramInstructions[14].grid(row=10, column=0, pady=5)
                paramEntries[14].grid(row=10, column=1, pady=5)
                paramInstructions[15].grid(row=11, column=0, pady=5)
                paramEntries[15].grid(row=11, column=1, pady=5)
            elif mode == "AAIR":
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[2].config(textvariable=AampStringVar)
                paramEntries[3].config(textvariable=APWStringVar)
                paramEntries[7].config(textvariable=ARPStringVar)
                paramEntries[9].config(textvariable=AsensStringVar)
                paramEntries[11].config(textvariable=PVARPStringVar)
                paramEntries[8].config(textvariable=MSRStringVar)
                paramEntries[12].config(textvariable=ActivityThreshStringVar)
                paramEntries[13].config(textvariable=RxtimeStringVar)
                paramEntries[14].config(textvariable=responseFactorStringVar)
                paramEntries[15].config(textvariable=recovTimeStringVar)
                for i in range(4):
                    paramInstructions[i].grid(row=i + 1, column=0, pady=5)
                    paramEntries[i].grid(row=i + 1, column=1, pady=5)
                paramInstructions[7].grid(row=5, column=0, pady=5)
                paramEntries[7].grid(row=5, column=1, pady=5)
                paramInstructions[9].grid(row=6, column=0, pady=5)
                paramEntries[9].grid(row=6, column=1, pady=5)
                paramInstructions[11].grid(row=7, column=0, pady=5)
                paramEntries[11].grid(row=7, column=1, pady=5)
                paramInstructions[8].grid(row=8, column=0, pady=5)
                paramEntries[8].grid(row=8, column=1, pady=5)
                paramInstructions[12].grid(row=9, column=0, pady=5)
                paramEntries[12].grid(row=9, column=1, pady=5)
                paramInstructions[13].grid(row=10, column=0, pady=5)
                paramEntries[13].grid(row=10, column=1, pady=5)
                paramInstructions[14].grid(row=11, column=0, pady=5)
                paramEntries[14].grid(row=11, column=1, pady=5)
                paramInstructions[15].grid(row=12, column=0, pady=5)
                paramEntries[15].grid(row=12, column=1, pady=5)
            # places submit button below all the other labels
            submit.grid(row=0, column=2, pady=5)

        def verifySubmit(user, mode):  # verifies and writes to database using sql
            checked = False  # variable for verification pass/fail
            errorMsg = ""  # error message empty string
            # all variables must get passed each condition for checked to return True or error message will show
            if LRLStringVar.get() >= 30 and LRLStringVar.get() <= 175:
                if (
                    URLStringVar.get() >= 50
                    and URLStringVar.get() <= 175
                    and URLStringVar.get() > LRLStringVar.get()
                ):
                    if mode == "AOO":
                        if AampStringVar.get() == 0 or (
                            AampStringVar.get() >= 0.1 and AampStringVar.get() <= 5
                        ):
                            if APWStringVar.get() >= 1 and APWStringVar.get() <= 30:
                                checked = True
                            else:
                                errorMsg = "APW has to be between 1 and 30ms"
                        else:
                            errorMsg = "A amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "VOO":
                        if VampStringVar.get() == 0 or (
                            VampStringVar.get() >= 0.1 and VampStringVar.get() <= 5
                        ):
                            if VPWStringVar.get() >= 1 and VPWStringVar.get() <= 30:
                                checked = True
                            else:
                                errorMsg = "VPW has to be between 1 and 30ms"
                        else:
                            errorMsg = "V amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "AAI":
                        if AampStringVar.get() == 0 or (
                            AampStringVar.get() >= 0.1 and AampStringVar.get() <= 5
                        ):
                            if APWStringVar.get() >= 1 and APWStringVar.get() <= 30:
                                if (
                                    ARPStringVar.get() >= 150
                                    and ARPStringVar.get() <= 500
                                ):
                                    if (
                                        AsensStringVar.get() >= 0.0
                                        and AsensStringVar.get() <= 5.0
                                    ):
                                        if (
                                            PVARPStringVar.get() >= 150
                                            and PVARPStringVar.get() <= 500
                                        ):
                                            checked = True
                                        else:
                                            errorMsg = (
                                                "PVARP has to be between 150 and 500"
                                            )
                                    else:
                                        errorMsg = "Asens has to be between 0 and 5"
                                else:
                                    errorMsg = "ARP has to be between 150 and 500"
                            else:
                                errorMsg = "APW has to be between 1 and 30"
                        else:
                            errorMsg = "A amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "VVI":
                        if VampStringVar.get() == 0 or (
                            VampStringVar.get() >= 0.1 and VampStringVar.get() <= 5
                        ):
                            if VPWStringVar.get() >= 1 and VPWStringVar.get() <= 30:
                                if (
                                    VRPStringVar.get() >= 150
                                    and VRPStringVar.get() <= 500
                                ):
                                    if (
                                        VsensStringVar.get() >= 0.0
                                        and VsensStringVar.get() <= 5.0
                                    ):
                                        checked = True
                                    else:
                                        errorMsg = "Vsens has to be between 0 and 5"
                                else:
                                    errorMsg = "VRP has to be between 150 and 500"
                            else:
                                errorMsg = "VPW has to be 0.05 or between 1 and 30ms"
                        else:
                            errorMsg = "V amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "AOOR":
                        if AampStringVar.get() == 0 or (
                            AampStringVar.get() >= 0.1 and AampStringVar.get() <= 5
                        ):
                            if APWStringVar.get() >= 1 and APWStringVar.get() <= 30:
                                if (
                                    MSRStringVar.get() >= 50
                                    and MSRStringVar.get() <= 175
                                ):
                                    if (
                                        ActivityThreshStringVar.get() >= 0
                                        and ActivityThreshStringVar.get() <= 6
                                    ):
                                        if (
                                            RxtimeStringVar.get() >= 10
                                            and RxtimeStringVar.get() <= 50
                                        ):
                                            if (
                                                responseFactorStringVar.get() >= 1
                                                and responseFactorStringVar.get() <= 16
                                            ):
                                                if (
                                                    recovTimeStringVar.get() >= 2
                                                    and recovTimeStringVar.get() <= 16
                                                ):
                                                    checked = True
                                                else:
                                                    errorMsg = "Recovery Time must be between 2 and 16"
                                            else:
                                                errorMsg = "Response Factor must be between 1 and 16"
                                        else:
                                            errorMsg = "Reaction time must be between 10 and 50"
                                    else:
                                        errorMsg = "Activity Threshold has to be between 0-6 for V-LOW to V-HIGH"
                                else:
                                    errorMsg = "MSR has to be between 50 and 175"
                            else:
                                errorMsg = "APW has to be between 1 and 30ms"
                        else:
                            errorMsg = "A amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "AAIR":
                        if AampStringVar.get() == 0 or (
                            AampStringVar.get() >= 0.1 and AampStringVar.get() <= 5
                        ):
                            if APWStringVar.get() >= 1 and APWStringVar.get() <= 30:
                                if (
                                    MSRStringVar.get() >= 50
                                    and MSRStringVar.get() <= 175
                                ):
                                    if (
                                        ActivityThreshStringVar.get() >= 0
                                        and ActivityThreshStringVar.get() <= 6
                                    ):
                                        if (
                                            RxtimeStringVar.get() >= 10
                                            and RxtimeStringVar.get() <= 50
                                        ):
                                            if (
                                                responseFactorStringVar.get() >= 1
                                                and responseFactorStringVar.get() <= 16
                                            ):
                                                if (
                                                    recovTimeStringVar.get() >= 2
                                                    and recovTimeStringVar.get() <= 16
                                                ):
                                                    if (
                                                        AsensStringVar.get() >= 0
                                                        and AsensStringVar.get() <= 5
                                                    ):
                                                        if (
                                                            ARPStringVar.get() >= 150
                                                            and ARPStringVar.get()
                                                            <= 500
                                                        ):
                                                            if (
                                                                PVARPStringVar.get()
                                                                >= 150
                                                                and PVARPStringVar.get()
                                                                <= 500
                                                            ):
                                                                checked = True
                                                            else:
                                                                errorMsg = "PVARP must be between 150 and 500"
                                                        else:
                                                            errorMsg = "ARP must be between 150 and 500"
                                                    else:
                                                        errorMsg = "Senstivity must be between 0 and 5"
                                                else:
                                                    errorMsg = "Recovery Time must be between 2 and 16"
                                            else:
                                                errorMsg = "Response Factor must be between 1 and 16"
                                        else:
                                            errorMsg = "Reaction time must be between 10 and 50"
                                    else:
                                        errorMsg = "Activity Threshold has to be between 0-6 for V-LOW to V-HIGH"
                                else:
                                    errorMsg = "MSR has to be between 50 and 175"
                            else:
                                errorMsg = "APW has to be between 1 and 30ms"
                        else:
                            errorMsg = "A amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "VVIR":
                        if VampStringVar.get() == 0 or (
                            VampStringVar.get() >= 0.1 and VampStringVar.get() <= 5
                        ):
                            if VPWStringVar.get() >= 1 and VPWStringVar.get() <= 30:
                                if (
                                    MSRStringVar.get() >= 50
                                    and MSRStringVar.get() <= 175
                                ):
                                    if (
                                        ActivityThreshStringVar.get() >= 0
                                        and ActivityThreshStringVar.get() <= 6
                                    ):
                                        if (
                                            RxtimeStringVar.get() >= 10
                                            and RxtimeStringVar.get() <= 50
                                        ):
                                            if (
                                                responseFactorStringVar.get() >= 1
                                                and responseFactorStringVar.get() <= 16
                                            ):
                                                if (
                                                    recovTimeStringVar.get() >= 2
                                                    and recovTimeStringVar.get() <= 16
                                                ):
                                                    if (
                                                        VsensStringVar.get() >= 0
                                                        and VsensStringVar.get() <= 5
                                                    ):
                                                        if (
                                                            VRPStringVar.get() >= 150
                                                            and VRPStringVar.get()
                                                            <= 500
                                                        ):
                                                            checked = True
                                                        else:
                                                            errorMsg = "VRP must be between 150 and 500"
                                                    else:
                                                        errorMsg = "Senstivity must be between 0 and 5"
                                                else:
                                                    errorMsg = "Recovery Time must be between 2 and 16"
                                            else:
                                                errorMsg = "Response Factor must be between 1 and 16"
                                        else:
                                            errorMsg = "Reaction time must be between 10 and 50"
                                    else:
                                        errorMsg = "Activity Threshold has to be between 0-6 for V-LOW to V-HIGH"
                                else:
                                    errorMsg = "MSR has to be between 50 and 175"
                            else:
                                errorMsg = "VPW has to be between 1 and 30ms"
                        else:
                            errorMsg = "V amplitude has to be 0 or between 0.1 and 5"
                    elif mode == "VOOR":
                        if VampStringVar.get() == 0 or (
                            VampStringVar.get() >= 0.1 and VampStringVar.get() <= 5
                        ):
                            if VPWStringVar.get() >= 1 and VPWStringVar.get() <= 30:
                                if (
                                    MSRStringVar.get() >= 50
                                    and MSRStringVar.get() <= 175
                                ):
                                    if (
                                        ActivityThreshStringVar.get() >= 0
                                        and ActivityThreshStringVar.get() <= 6
                                    ):
                                        if (
                                            RxtimeStringVar.get() >= 10
                                            and RxtimeStringVar.get() <= 50
                                        ):
                                            if (
                                                responseFactorStringVar.get() >= 1
                                                and responseFactorStringVar.get() <= 16
                                            ):
                                                if (
                                                    recovTimeStringVar.get() >= 2
                                                    and recovTimeStringVar.get() <= 16
                                                ):
                                                    checked = True
                                                else:
                                                    errorMsg = "Recovery Time must be between 2 and 16"
                                            else:
                                                errorMsg = "Response Factor must be between 1 and 16"
                                        else:
                                            errorMsg = "Reaction time must be between 10 and 50"
                                    else:
                                        errorMsg = "Activity Threshold has to be between 0-6 for V-LOW to V-HIGH"
                                else:
                                    errorMsg = "MSR has to be between 50 and 175"
                            else:
                                errorMsg = "VPW has to be between 1 and 30ms"
                        else:
                            errorMsg = "V amplitude has to be 0 or between 0.1 and 5"
                else:
                    errorMsg = "URL has to be between 50 and 175 and bigger then LRL"
            else:
                errorMsg = "LRL has to be between 30 and 175"

            # checkComs = isConnected()
            # if (checkComs[0] == False):
            #     checked = False
            #     errorMsg = "No Device Connected"s

            if checked == True:
                if mode == "AOO":
                    # verify values code
                    try:
                        paramList = []
                        # appending value to parameter list
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(AampStringVar.get())
                        paramList.append(APWStringVar.get())

                    except:  # if input is not a number- will output message to user and not submit
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "VOO":  # same as AOO
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(VampStringVar.get())
                        paramList.append(VPWStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "AOOR":  # same as AOO
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(AampStringVar.get())
                        paramList.append(APWStringVar.get())
                        paramList.append(MSRStringVar.get())
                        paramList.append(ActivityThreshStringVar.get())
                        paramList.append(RxtimeStringVar.get())
                        paramList.append(responseFactorStringVar.get())
                        paramList.append(recovTimeStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "AAIR":  # same as AOO
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(AampStringVar.get())
                        paramList.append(APWStringVar.get())
                        paramList.append(ARPStringVar.get())
                        paramList.append(MSRStringVar.get())
                        paramList.append(AsensStringVar.get())
                        paramList.append(PVARPStringVar.get())
                        paramList.append(ActivityThreshStringVar.get())
                        paramList.append(RxtimeStringVar.get())
                        paramList.append(responseFactorStringVar.get())
                        paramList.append(recovTimeStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "VVIR":  # same as AOO
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(VampStringVar.get())
                        paramList.append(VPWStringVar.get())
                        paramList.append(VRPStringVar.get())
                        paramList.append(MSRStringVar.get())
                        paramList.append(VsensStringVar.get())
                        paramList.append(ActivityThreshStringVar.get())
                        paramList.append(RxtimeStringVar.get())
                        paramList.append(responseFactorStringVar.get())
                        paramList.append(recovTimeStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "VOOR":  # same as AOO
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(VampStringVar.get())
                        paramList.append(VPWStringVar.get())
                        paramList.append(MSRStringVar.get())
                        paramList.append(ActivityThreshStringVar.get())
                        paramList.append(RxtimeStringVar.get())
                        paramList.append(responseFactorStringVar.get())
                        paramList.append(recovTimeStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "VVI":
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(VampStringVar.get())
                        paramList.append(VPWStringVar.get())
                        paramList.append(VRPStringVar.get())
                        paramList.append(VsensStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                elif mode == "AAI":
                    # verify values code
                    try:
                        paramList = []
                        paramList.append(LRLStringVar.get())
                        paramList.append(URLStringVar.get())
                        paramList.append(AampStringVar.get())
                        paramList.append(APWStringVar.get())
                        paramList.append(ARPStringVar.get())
                        paramList.append(AsensStringVar.get())
                        paramList.append(PVARPStringVar.get())
                    except:
                        messagebox.showinfo(message="Inputs must be a number")
                else:  # if mode is not one of the 4 something went wrong in logic
                    print("something went wrong :(")
                # sets parameters to SQL database
                setParams(user, paramList, mode)
                # sends to device
                dataSend = [
                    LRLStringVar.get(),
                    AampStringVar.get(),
                    APWStringVar.get(),
                    AsensStringVar.get(),
                    ARPStringVar.get(),
                    VampStringVar.get(),
                    VPWStringVar.get(),
                    VsensStringVar.get(),
                    VRPStringVar.get(),
                    RxtimeStringVar.get(),
                    recovTimeStringVar.get(),
                    mode,
                    URLStringVar.get(),
                ]
                # for count, param in enumerate(dataSend):
                #     if (param == None or param == ""):
                #         dataSend[count] = 0.0
                sendData(dataSend)
                # resets entry boxes
                LRLStringVar.set(0.0)
                URLStringVar.set(0.0)
                AampStringVar.set(0.0)
                APWStringVar.set(0.0)
                VampStringVar.set(0.0)
                VPWStringVar.set(0.0)
                ARPStringVar.set(0.0)
                VRPStringVar.set(0.0)
                MSRStringVar.set(0.0)
                AsensStringVar.set(0.0)
                VsensStringVar.set(0.0)
                PVARPStringVar.set(0.0)
                ActivityThreshStringVar.set(0.0)
                RxtimeStringVar.set(0.0)
                responseFactorStringVar.set(0.0)
                recovTimeStringVar.set(0.0)
                # outputs to user success
                messagebox.showinfo(message="Parameters Set")
            else:
                messagebox.showinfo(message=errorMsg)

        def backPressed():  # back button pressed forget unneeded labels and regrid the read and set buttons
            parameterlabel.config(text="")
            parameterlabel.grid_forget()
            readButt.grid(row=1, column=1, pady=5)
            setButt.grid(row=2, column=1, pady=5)
            submit.grid_forget()
            # enumerate to get index of string list to forget them
            for i, p in enumerate(paramArr):
                paramEntries[i].config(textvariable=emptyStringVar)
                paramInstructions[i].grid_forget()
                paramEntries[i].grid_forget()

            controller.dispFrame("afterLogin")  # change page

        # widgets
        parameterlabel = tk.Label(
            self,
            text="",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )  # Label for displaying parameters in read

        paramArr = [
            "LRL",
            "URL",
            "Aamp",
            "APW",
            "VAMP",
            "VPW",
            "VRP",
            "ARP",
            "MSR",
            "Asens",
            "Vsens",
            "PVARP",
            "Activity Threshold",
            "Rx time",
            "Response Factor",
            "Recovery Time",
        ]  # array of parameters
        paramEntries = []  # entry box array for parameter
        paramInstructions = []  # entry box instructions for parameters
        emptyStringVar = tk.StringVar(self, "")  # empty StringVar
        submit = tk.Button(
            self,
            text="Submit",  # submit button calls verifySubmit when clicked
            width=20,
            height=2,
            command=lambda: verifySubmit(
                controller.sharedUser["username"].get(),
                controller.sharedUser["mode"].get(),
            ),
        )
        # assigning list for entry and instructions to appropriate parameter
        for index, param in enumerate(paramArr):
            paramInstructions.append(
                tk.Label(
                    self,
                    text=paramArr[index],
                    fg="#F2BA49",
                    bg=BGCOLOR,
                    justify="center",
                    font="default, 25",
                )
            )
            paramEntries.append(
                tk.Entry(
                    self,
                    bg="#FFFF9F",
                    fg=BGCOLOR,
                    textvariable=emptyStringVar,
                    width=20,
                )
            )

        title = tk.Label(
            self,
            textvariable=controller.sharedUser["mode"],
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )  # Mode title
        title.grid(row=0, column=1, pady=10, padx=200)
        backButt = tk.Button(
            self, text="Back", width=5, height=2, command=lambda: backPressed()
        )
        backButt.grid(row=0, column=0, pady=5)  # back button calls backPressed
        readButt = tk.Button(
            self,
            text="Read Parameters",
            width=20,
            height=2,
            command=lambda: displayParam(
                controller.sharedUser["username"].get(),
                controller.sharedUser["mode"].get(),
            ),
        )
        # read parameter button calls displayParam
        readButt.grid(row=1, column=1, pady=5)
        setButt = tk.Button(
            self,
            text="Set Parameters",
            width=20,
            height=2,
            command=lambda: setParam(controller.sharedUser["mode"].get()),
        )
        setButt.grid(row=2, column=1, pady=5)  # setBUtt button calls setParam


class afterLogin(tk.Frame):  # page after login success
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        def modeSelect(mode):  # sets mode depending on button press
            if mode == "AOO":
                controller.sharedUser["mode"].set("AOO")
            elif mode == "VOO":
                controller.sharedUser["mode"].set("VOO")
            elif mode == "AAI":
                controller.sharedUser["mode"].set("AAI")
            elif mode == "VVI":
                controller.sharedUser["mode"].set("VVI")
            elif mode == "AOOR":
                controller.sharedUser["mode"].set("AOOR")
            elif mode == "VOOR":
                controller.sharedUser["mode"].set("VOOR")
            elif mode == "AAIR":
                controller.sharedUser["mode"].set("AAIR")
            elif mode == "VVIR":
                controller.sharedUser["mode"].set("VVIR")
            controller.dispFrame("modeP")  # calls modeP page to front
            # Connection display

        connected = isConnected()[0]
        different = isDifferent(str(controller.sharedUser["username"]))

        def refreshConnection():  # refresh connection for device connection and id checking- will be improved with serial comms
            # connected = True  # testing purposes change to true as simulated connection
            # different = True  # testing purposes change value
            connected = isConnected()[0]
            different = isDifferent(str(controller.sharedUser["username"]))
            connection.set("Connected" if connected else "Disconnected")
            # will show different device label if different ids- from serialCom.py
            if different == True and connected == True:
                showDifferent.grid(row=1, column=3)
            else:
                showDifferent.grid_forget()  # removes different label from user view

        connection = tk.StringVar(
            self, "Connected" if connected else "Disconnected"
        )  # connection stringVar that gets value from initial value of connected from serialCom.py
        showConnection = tk.Label(
            self,
            textvariable=connection,
            fg="Blue",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        showConnection.grid(row=0, column=3)

        showDifferent = tk.Label(
            self,
            text="New Pacemaker",
            fg="Blue",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        # shows different label if both different and connected are true
        if different == True and connected == True:
            showDifferent.grid(row=1, column=3)

        refreshButt = tk.Button(
            self, text="Check Connection", height=2, command=lambda: refreshConnection()
        )  # user manually has to press refresh button for now
        refreshButt.grid(row=2, column=3)

        def signOut():  # signs out user by going to welcome page and removing username history from shared variable
            username.config(
                textvariable=controller.sharedUser["username"].set(""))
            controller.dispFrame("welcomeP")

        user = tk.Label(
            self,
            text="User:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )  # user label on screen to display "user:"
        user.grid(row=0, column=2, pady=10, padx=150)
        username = tk.Label(
            self,
            textvariable=controller.sharedUser["username"],
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )  # displays username on screen
        username.grid(row=1, column=2, padx=150)
        # graph buttons and method

        def gMode(gType):
            if gType == "A":
                graphFunc("A")
            if gType == "V":
                graphFunc("V")
            if gType == "B":
                graphFunc("B")

        gAButt = tk.Button(
            self, text="Atrium Graph", width=7, height=2, command=lambda: gMode("A")
        )  # signout button calls signOut
        gAButt.grid(row=2, column=2, pady=5)

        gVButt = tk.Button(
            self, text="Ventrical Graph", width=7, height=2, command=lambda: gMode("V")
        )  # signout button calls signOut
        gVButt.grid(row=3, column=2, pady=5)

        gBButt = tk.Button(
            self, text="Both Graphs", width=7, height=2, command=lambda: gMode("B")
        )  # signout button calls signOut
        gBButt.grid(row=4, column=2, pady=5)
        # back button
        soButt = tk.Button(
            self, text="Sign Out", width=5, height=2, command=lambda: signOut()
        )  # signout button calls signOut
        soButt.grid(row=0, column=0, pady=5)
        AOO = tk.Button(
            self, text="AOO", width=5, height=2, command=lambda: modeSelect("AOO")
        )  # different mode buttons that calls modeSelect and passes mode
        AOO.grid(row=1, column=0, pady=5)
        VOO = tk.Button(
            self, text="VOO", width=5, height=2, command=lambda: modeSelect("VOO")
        )
        VOO.grid(row=1, column=1, pady=5)
        AAI = tk.Button(
            self, text="AAI", width=5, height=2, command=lambda: modeSelect("AAI")
        )
        AAI.grid(row=2, column=0, pady=5)
        VVI = tk.Button(
            self, text="VVI", width=5, height=2, command=lambda: modeSelect("VVI")
        )
        VVI.grid(row=2, column=1, pady=5)
        AOOR = tk.Button(
            self, text="AOOR", width=5, height=2, command=lambda: modeSelect("AOOR")
        )
        AOOR.grid(row=3, column=0, pady=5)
        VOOR = tk.Button(
            self, text="VOOR", width=5, height=2, command=lambda: modeSelect("VOOR")
        )
        VOOR.grid(row=3, column=1, pady=5)
        AAIR = tk.Button(
            self, text="AAIR", width=5, height=2, command=lambda: modeSelect("AAIR")
        )
        AAIR.grid(row=4, column=0, pady=5)
        VVIR = tk.Button(
            self, text="VVIR", width=5, height=2, command=lambda: modeSelect("VVIR")
        )
        VVIR.grid(row=4, column=1, pady=5)


class loginP(tk.Frame):  # login page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        def clearBox():  # removes all values from entry but also affects variable attached to them!!
            user.delete(0, tk.END)
            password.delete(0, tk.END)

        # presses login button calls function from options.py
        def loginPressed(user, password):
            loginInfo = login(user, password)
            # based on code- sent through to next page or has to properly login
            logCode = loginInfo[0]
            logMsg = loginInfo[1]
            if logCode == 2:  # success
                enterPass.set("")  # forgets password
                controller.dispFrame("afterLogin")  # goes to next page
            elif logCode == 1:  # Issue type 1
                # shows error message to user and try again
                messagebox.showinfo(message=logMsg)
                clearBox()
                controller.dispFrame("welcomeP")
            else:  # Issue type 0 or unknown
                messagebox.showinfo(message=logMsg)
                clearBox()

        def signOut():  # signout function for login page- i.e clears fields and goes to welcome screen
            clearBox()
            controller.dispFrame("welcomeP")

        # Title label
        title = tk.Label(
            self,
            text="Login",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )  # Login title
        title.grid(row=0, column=1, pady=10, padx=200)
        # button for option select on welcome screen
        welcomeButt = tk.Button(
            self, text="To Main", width=5, height=2, command=lambda: signOut()
        )

        enterPass = tk.StringVar()  # password StringVar
        user = tk.Entry(
            self,
            bg="#FFFF9F",
            fg=BGCOLOR,  # username field
            textvariable=controller.sharedUser["username"],
            width=20,
        )
        password = tk.Entry(
            self,
            bg="#FFFF9F",
            fg=BGCOLOR,  # password field
            textvariable=enterPass,
            width=20,
            show="*",
        )
        userIns = tk.Label(
            self,
            text="Username:",
            fg="#F2BA49",
            bg=BGCOLOR,  # instructions
            justify="center",
            font="default, 25",
        )
        passIns = tk.Label(
            self,
            text="Password:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        submit = tk.Button(
            self,
            text="Login",  # login button calls loginPressed()
            width=5,
            height=2,
            command=lambda: loginPressed(
                controller.sharedUser["username"].get(), enterPass.get()
            ),
        )
        # placement of labels and buttons
        welcomeButt.grid(row=0, column=0, pady=5)
        user.grid(row=2, column=1, pady=5)
        password.grid(row=3, column=1, pady=10)
        userIns.grid(row=2, column=0)
        passIns.grid(row=3, column=0)
        submit.grid(row=4, column=1)


class signupP(tk.Frame):  # signup frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)

        self.controller = controller
        # submit control

        def clearBox():  # clears both passwords
            user.delete(0, tk.END)
            password.delete(0, tk.END)
            passwordTwo.delete(0, tk.END)

        def signupcheck(user, pw, pwconf):  # calls options function signup()
            clearBox()
            # list of code and message of signup() results
            signupRecieved = signup(user, pw, pwconf)
            checkCode = signupRecieved[0]
            messageInfo = signupRecieved[1]
            messagebox.showinfo(message=messageInfo)
            if checkCode == 2:  # can login
                controller.dispFrame("loginP")
            elif checkCode == 1:  # does nothing because error is retyping issue
                pass
            else:  # goes back to welcome screen option=0
                controller.dispFrame("welcomeP")

        # Title label
        title = tk.Label(
            self,
            text="Signup",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        title.grid(row=0, column=1, pady=10, padx=200)
        # buttons and entries
        welcomeButt = tk.Button(
            self,
            text="To Main",
            width=5,
            height=2,
            command=lambda: controller.dispFrame("welcomeP"),
        )
        enterUser = tk.StringVar()
        enterPass = tk.StringVar()  # stringVars for field entries
        enterPassTwo = tk.StringVar()
        # entry boxes
        user = tk.Entry(
            self, bg="#FFFF9F", fg=BGCOLOR, textvariable=enterUser, width=20
        )
        password = tk.Entry(
            self, bg="#FFFF9F", fg=BGCOLOR, textvariable=enterPass, width=20, show="*"
        )
        passwordTwo = tk.Entry(
            self,
            bg="#FFFF9F",
            fg=BGCOLOR,
            textvariable=enterPassTwo,
            width=20,
            show="*",
        )
        submit = tk.Button(
            self,
            text="Submit",
            width=5,
            height=2,
            command=lambda: signupcheck(
                enterUser.get(), enterPass.get(), enterPassTwo.get()
            ),
        )
        # labels
        userIns = tk.Label(
            self,
            text="Username:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        passIns = tk.Label(
            self,
            text="Password:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        passInsTwo = tk.Label(
            self,
            text="Confirm Password:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        # placement
        welcomeButt.grid(row=0, column=0, pady=5)
        user.grid(row=2, column=1, pady=5)
        password.grid(row=3, column=1, pady=10)
        passwordTwo.grid(row=4, column=1, pady=10)
        userIns.grid(row=2, column=0)
        passIns.grid(row=3, column=0)
        passInsTwo.grid(row=4, column=0)
        submit.grid(row=5, column=1)


class deleteP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        def clearBox():
            user.delete(0, tk.END)
            password.delete(0, tk.END)

        def deleteUser(user, pw):  # calls delete() method in options
            clearBox()
            deleteMsg = delete(user, pw)
            messagebox.showinfo(message=deleteMsg)
            controller.dispFrame("welcomeP")  # goes back to welcome page

        # Title label
        title = tk.Label(
            self,
            text="Delete",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        title.grid(row=0, column=1, pady=10, padx=200)
        # buttons and entries
        welcomeButt = tk.Button(
            self,
            text="To Main",
            width=5,
            height=2,
            command=lambda: controller.dispFrame("welcomeP"),
        )
        enterUser = tk.StringVar()  # user password entry
        enterPass = tk.StringVar()
        user = tk.Entry(
            self, bg="#FFFF9F", fg=BGCOLOR, textvariable=enterUser, width=20
        )
        password = tk.Entry(
            self, bg="#FFFF9F", fg=BGCOLOR, textvariable=enterPass, width=20, show="*"
        )
        submit = tk.Button(
            self,
            text="Submit",  # submit button calls deleteUser()
            width=5,
            height=2,
            command=lambda: deleteUser(enterUser.get(), enterPass.get()),
        )
        # labels
        userIns = tk.Label(
            self,
            text="Username:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        passIns = tk.Label(
            self,
            text="Password:",
            fg="#F2BA49",
            bg=BGCOLOR,
            justify="center",
            font="default, 25",
        )
        # placement
        welcomeButt.grid(row=0, column=0, pady=5)
        user.grid(row=2, column=1, pady=5)
        password.grid(row=3, column=1, pady=10)
        userIns.grid(row=2, column=0)
        passIns.grid(row=3, column=0)
        submit.grid(row=5, column=1)


# mode page


if __name__ == "__main__":
    app = gui()  # gui instance
    app.mainloop()  # mainloop runs program
