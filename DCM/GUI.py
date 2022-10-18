# from cgitb import text
from email.policy import EmailPolicy
import enum
import tkinter as tk
from tkinter import messagebox
from options import *
from storeAttributes import *
from serialCom import *
BGCOLOR = '#800000'


class gui (tk.Tk):  # tk.TK is root
    # controller for pages
    # *args and **kwargs can receive multiple parameters kwargs is for named values
    def __init__(self, *args, **kwargs):
        # init for tkinter functionality (superclass)
        tk.Tk.__init__(self, *args, **kwargs)
        self.sharedUser = {"username": tk.StringVar(),
                           "mode": tk.StringVar()}
        container = tk.Frame()  # container for frames
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.pageInfo = {}  # empty dictionary for page name and object
        # signupP, deleteP]  # array of class objects
        for page in (welcomeP, loginP, signupP, deleteP, afterLogin, modeP):
            pageName = page.__name__  # magic  method to get object name -pythons cool
            # parent as container for frame, with self as controller to use function in gui
            frame = page(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky='nesw')
            # pagename dictionary with frame objects
            self.pageInfo[pageName] = frame
        self.dispFrame('loginP')  # show welcome first

    def dispFrame(self, pageName):  # display frame based on name
        page = self.pageInfo[pageName]
        page.tkraise()


class welcomeP(tk.Frame):  # Frame is parent
    def __init__(self, parent, controller):  # init object as specified in gui
        # init frame to get tkinter frame properties
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller
        self.controller.title('Heart Pacer 26')
        # welcome label
        title = tk.Label(self, text='Welcome', fg='#F2BA49', bg=BGCOLOR,
                         justify='center', font="default, 25")
        # title.place(x=400, y=100, anchor=CENTER)
        title.pack(pady=10, padx=300)
        # button for option select on welcome screen
        loginButt = tk.Button(self, text="Login",
                              width=20, height=2, command=lambda: controller.dispFrame("loginP"))
        signButt = tk.Button(self, text="Signup",
                             width=20, height=2, command=lambda: controller.dispFrame("signupP"))
        deleteButt = tk.Button(
            self, text="Delete", width=20, height=2, command=lambda: controller.dispFrame("deleteP"))
        loginButt.pack(pady=5)
        signButt.pack(pady=5)
        deleteButt.pack(pady=5)


class modeP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        LRLStringVar = tk.StringVar()
        URLStringVar = tk.StringVar()
        AampStringVar = tk.StringVar()
        APWStringVar = tk.StringVar()
        VampStringVar = tk.StringVar()
        VPWStringVar = tk.StringVar()
        ARPStringVar = tk.StringVar()
        VRPStringVar = tk.StringVar()

        def displayParam(userName, mode):
            readButt.grid_remove()
            setButt.grid_remove()
            if (mode == "AOO"):
                parameterList = getParams(userName, mode)
                if (parameterList == None):
                    parameterlabel.config(text="no parameters")
                else:

                    # get from text file
                    pLabelText = "LRL: " + \
                        str(parameterList[0])+"\n URL: "+str(parameterList[1])+"\n AAMP: " + \
                        str(parameterList[2])+"\n APW: " + \
                        str(parameterList[3])
                    parameterlabel.config(text=pLabelText)
            elif (mode == ""):
                parameterlabel.config(text="")
            else:
                parameterlabel.config(text="diff mode")

            parameterlabel.grid(row=2, column=1)

        def setParam(mode):
            readButt.grid_remove()
            setButt.grid_remove()
            if (mode == 'AOO'):
                paramEntries[0].config(textvariable=LRLStringVar)
                paramEntries[1].config(textvariable=URLStringVar)
                paramEntries[2].config(textvariable=AampStringVar)
                paramEntries[3].config(textvariable=APWStringVar)
                for i in range(4):
                    paramInstructions[i].grid(row=i+1, column=0, pady=5)
                    paramEntries[i].grid(row=i+1, column=1, pady=5)
            submit.grid(row=5, column=1, pady=5)

        def verifySubmit(user, mode):
            if (mode == "AOO"):
                # verify values code
                paramList = []
                print(LRLStringVar.get()+" LRL should be 1")
                paramList.append(LRLStringVar.get())
                paramList.append(URLStringVar.get())
                paramList.append(AampStringVar.get())
                paramList.append(APWStringVar.get())
            setParams(user, paramList, mode)
            LRLStringVar.set("")
            URLStringVar.set("")
            AampStringVar.set("")
            APWStringVar.set("")
            VampStringVar.set("")
            VPWStringVar.set("")
            ARPStringVar.set("")
            VRPStringVar.set("")
            messagebox.showinfo(message="Success")

        def backPressed():
            parameterlabel.config(text="")
            parameterlabel.grid_forget()
            readButt.grid(row=1, column=1, pady=5)
            setButt.grid(row=2, column=1, pady=5)
            submit.grid_forget()
            for i, p in enumerate(paramArr):
                paramEntries[i].config(textvariable=emptyStringVar)
                paramInstructions[i].grid_forget()
                paramEntries[i].grid_forget()

            controller.dispFrame("afterLogin")

        # widgets
        parameterlabel = tk.Label(self, text="", fg='#F2BA49', bg=BGCOLOR,
                                  justify='center', font="default, 25")

        paramArr = ['LRL', 'URL', 'Aamp', 'APW', 'VAMP', 'VPW', 'VRP', 'ARP']
        paramEntries = []
        paramInstructions = []
        emptyStringVar = tk.StringVar(self, "")
        submit = tk.Button(self, text="Submit",
                           width=20, height=2, command=lambda: verifySubmit(controller.sharedUser["username"].get(), controller.sharedUser["mode"].get()))
        for index, param in enumerate(paramArr):
            paramInstructions.append(tk.Label(self, text=paramArr[index], fg='#F2BA49', bg=BGCOLOR,
                                              justify='center', font="default, 25"))
            paramEntries.append(tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                                         textvariable=emptyStringVar, width=20))

        title = tk.Label(self, textvariable=controller.sharedUser["mode"], fg='#F2BA49', bg=BGCOLOR,
                         justify='center', font="default, 25")
        title.grid(row=0, column=1, pady=10, padx=200)
        backButt = tk.Button(self, text="Back",
                             width=5, height=2, command=lambda: backPressed())
        backButt.grid(row=0, column=0, pady=5)
        readButt = tk.Button(self, text="Read Parameters",
                             width=20, height=2, command=lambda: displayParam(controller.sharedUser["username"].get(), controller.sharedUser["mode"].get()))
        readButt.grid(row=1, column=1, pady=5)
        setButt = tk.Button(self, text="Set Parameters",
                                       width=20, height=2, command=lambda: setParam(controller.sharedUser["mode"].get()))
        setButt.grid(row=2, column=1, pady=5)


class afterLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        def modeSelect(mode):
            if (mode == "AOO"):
                controller.sharedUser["mode"].set("AOO")
            elif (mode == "VOO"):
                controller.sharedUser["mode"].set("VOO")
            elif (mode == "AAI"):
                controller.sharedUser["mode"].set("AII")
            elif (mode == "VVI"):
                controller.sharedUser["mode"].set("VVI")
            controller.dispFrame("modeP")

        def refreshConnection():
            connected = True  # testing purposes
            connection.set("Connected" if connected else "Disconnected")

        def signOut():
            username.config(
                textvariable=controller.sharedUser["username"].set(""))
            controller.dispFrame("welcomeP")

        connection = tk.StringVar(
            self, "Connected" if connected else "Disconnected")
        showConnection = tk.Label(self, textvariable=connection, fg='Blue', bg=BGCOLOR,
                                  justify='center', font="default, 25")
        showConnection.grid(row=0, column=3)
        refreshButt = tk.Button(self, text="Check Connection", height=2,
                                command=lambda: refreshConnection())
        refreshButt.grid(row=1, column=3)
        user = tk.Label(self, text="User:", fg='#F2BA49', bg=BGCOLOR,
                        justify='center', font="default, 25")
        user.grid(row=0, column=2, pady=10, padx=150)
        username = tk.Label(self, textvariable=controller.sharedUser["username"], fg='#F2BA49', bg=BGCOLOR,
                            justify='center', font="default, 25")
        username.grid(row=1, column=2, padx=150)
        # back button
        soButt = tk.Button(self, text="Sign Out",
                           width=5, height=2, command=lambda: signOut())
        soButt.grid(row=0, column=0, pady=5)
        AOO = tk.Button(self, text="AOO", width=5, height=2,
                        command=lambda: modeSelect("AOO"))
        AOO.grid(row=1, column=0, pady=5)
        VOO = tk.Button(self, text="VOO", width=5, height=2,
                        command=lambda: modeSelect("VOO"))
        VOO.grid(row=1, column=1, pady=5)
        AAI = tk.Button(self, text="AAI", width=5, height=2,
                        command=lambda: modeSelect("AAI"))
        AAI.grid(row=2, column=0, pady=5)
        VVI = tk.Button(self, text="VVI", width=5, height=2,
                        command=lambda: modeSelect("VVI"))
        VVI.grid(row=2, column=1, pady=5)


class loginP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)
        self.controller = controller

        def clearBox():
            user.delete(0, tk.END)
            password.delete(0, tk.END)

        def loginPressed(user, password):
            loginInfo = login(user, password)
            logCode = loginInfo[0]
            logMsg = loginInfo[1]
            if (logCode == 2):  # success
                enterPass.set("")
                controller.dispFrame("afterLogin")
            elif (logCode == 1):  # Issue type 1
                messagebox.showinfo(message=logMsg)
                clearBox()
                controller.dispFrame("welcomeP")
            else:  # Issue type 0 or unknown
                messagebox.showinfo(message=logMsg)
                clearBox()

        def signOut():
            clearBox()
            controller.dispFrame("welcomeP")
        # Title label
        title = tk.Label(self, text='Login', fg='#F2BA49', bg=BGCOLOR,
                         justify='center', font="default, 25")
        title.grid(row=0, column=1, pady=10, padx=200)
        # button for option select on welcome screen
        welcomeButt = tk.Button(self, text="To Main",
                                width=5, height=2, command=lambda: signOut())
        # enterUser = tk.StringVar()
        enterPass = tk.StringVar()
        user = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                        textvariable=controller.sharedUser["username"], width=20)
        password = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                            textvariable=enterPass, width=20)
        userIns = tk.Label(self, text='Username:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        passIns = tk.Label(self, text='Password:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        submit = tk.Button(self, text="Login",
                           width=5, height=2, command=lambda: loginPressed(controller.sharedUser["username"].get(), enterPass.get()))
        # placement
        welcomeButt.grid(row=0, column=0, pady=5)
        user.grid(row=2, column=1, pady=5)
        password.grid(row=3, column=1, pady=10)
        userIns.grid(row=2, column=0)
        passIns.grid(row=3, column=0)
        submit.grid(row=4, column=1)


class signupP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BGCOLOR)

        self.controller = controller
        # submit control

        def clearBox():
            user.delete(0, tk.END)
            password.delete(0, tk.END)
            passwordTwo.delete(0, tk.END)

        def signupcheck(user, pw, pwconf):
            clearBox()
            signupRecieved = signup(user, pw, pwconf)
            checkCode = signupRecieved[0]
            messageInfo = signupRecieved[1]
            messagebox.showinfo(message=messageInfo)
            if (checkCode == 2):
                controller.dispFrame("loginP")
            elif (checkCode == 1):
                pass
            else:
                controller.dispFrame("welcomeP")
        # Title label
        title = tk.Label(self, text='Signup', fg='#F2BA49', bg=BGCOLOR,
                         justify='center', font="default, 25")
        title.grid(row=0, column=1, pady=10, padx=200)
        # buttons and entries
        welcomeButt = tk.Button(self, text="To Main",
                                width=5, height=2, command=lambda: controller.dispFrame("welcomeP"))
        enterUser = tk.StringVar()
        enterPass = tk.StringVar()
        enterPassTwo = tk.StringVar()
        user = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                        textvariable=enterUser, width=20)
        password = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                            textvariable=enterPass, width=20)
        passwordTwo = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                               textvariable=enterPassTwo, width=20)
        submit = tk.Button(self, text="Submit",
                           width=5, height=2, command=lambda: signupcheck(enterUser.get(), enterPass.get(), enterPassTwo.get()))
        # labels
        userIns = tk.Label(self, text='Username:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        passIns = tk.Label(self, text='Password:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        passInsTwo = tk.Label(self, text='Password:', fg='#F2BA49', bg=BGCOLOR,
                              justify='center', font="default, 25")
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
        # submit control

        def clearBox():
            user.delete(0, tk.END)
            password.delete(0, tk.END)

        def deleteUser(user, pw):
            clearBox()
            deleteMsg = delete(user, pw)
            messagebox.showinfo(message=deleteMsg)
            controller.dispFrame("welcomeP")
        # Title label
        title = tk.Label(self, text='Delete', fg='#F2BA49', bg=BGCOLOR,
                         justify='center', font="default, 25")
        title.grid(row=0, column=1, pady=10, padx=200)
        # buttons and entries
        welcomeButt = tk.Button(self, text="To Main",
                                width=5, height=2, command=lambda: controller.dispFrame("welcomeP"))
        enterUser = tk.StringVar()
        enterPass = tk.StringVar()
        user = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                        textvariable=enterUser, width=20)
        password = tk.Entry(self, bg="#FFFF9F", fg=BGCOLOR,
                            textvariable=enterPass, width=20)
        submit = tk.Button(self, text="Submit",
                           width=5, height=2, command=lambda: deleteUser(enterUser.get(), enterPass.get()))
        # labels
        userIns = tk.Label(self, text='Username:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        passIns = tk.Label(self, text='Password:', fg='#F2BA49', bg=BGCOLOR,
                           justify='center', font="default, 25")
        # placement
        welcomeButt.grid(row=0, column=0, pady=5)
        user.grid(row=2, column=1, pady=5)
        password.grid(row=3, column=1, pady=10)
        userIns.grid(row=2, column=0)
        passIns.grid(row=3, column=0)
        submit.grid(row=5, column=1)

# mode page


if __name__ == "__main__":
    app = gui()
    app.mainloop()
