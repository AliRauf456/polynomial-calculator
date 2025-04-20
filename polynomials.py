#importing neccesary libraries
from tkinter import *

class PolynomialsFrames:
    # Initializes the class instance
    def __init__(self, idx , master):
        # Sets the master attribute to the passed in master object
        self.master = master
        # Creates a label widget displaying 'Enter Coeffecients for..' in the specified font and position
        label = Label(master.Frames[1], text='Enter Coeffecients for..', font='Arial 18 bold')
        label.config(bg=master.primary[master.mode], fg=master.primaryfg[master.mode])
        label.place(x=550, y=100)
        # Creates a 'Next' button widget in the specified background and foreground colors with the specified font, height, and width, and sets its command to the getData method
        self.savebutton = Button(master.Frames[1], text='Next', bg='#0c6375', fg='white')
        self.savebutton.config(height=2, width=14, font='Arial 14 bold')
        self.savebutton.config(command=self.getData)
        
        # Determines the equation mode based on the passed in idx value and calls the corresponding method
        if(idx == 'Quadratic'):
            master.eqMode=0
            self.Quadratic()
        if(idx == 'Cubic'):
            master.eqMode=1
            self.Cubic()
        if(idx == 'Quartic'):
            master.eqMode=2
            self.Quartic()

    # Creates a label widget with the specified text and coordinates
    def labelMaker(self, text, coord):
        master = self.master
        label = Label(master.Frames[1], text=text, font='Arial 22 bold')
        label.config(bg=master.primary[master.mode], fg=master.primaryfg[master.mode])
        label.place(x=coord[0], y=coord[1])

    # Creates an entry widget at the specified coordinates and returns it
    def entryMaker(self, coord):
        master = self.master
        entry = Entry(master.Frames[1], font='Arial 20 bold', width=10)
        entry.place(x=coord[0], y=coord[1])
        return entry

    # Creates the GUI elements for the Quadratic equation mode
    def Quadratic(self):
        # Creates the necessary labels and entry widgets for the Quadratic equation mode
        self.labelMaker('x²',[550, 200])
        self.labelMaker('x',[550, 300])
        self.labelMaker('constant',[500, 400])
        entryQdx2 = self.entryMaker([650, 200])
        entryQdx = self.entryMaker([650, 300])
        entryQdconst = self.entryMaker([650, 400])
        # Places the 'Next' button widget on the GUI
        self.savebutton.place(x=600, y=500)
        
        # Stores the Quadratic equation mode entry widgets in the QuadEntries list attribute
        self.QuadEntries = [entryQdx2, entryQdx, entryQdconst]
        pass

    def Cubic(self):
        # create labels for each coefficient
        self.labelMaker('x³',[550, 200])
        self.labelMaker('x²',[550, 280])
        self.labelMaker('x',[550, 360])
        self.labelMaker('constant',[500, 440])
        
        # create entry fields for each coefficient and save them
        entryCbx3 = self.entryMaker([650, 200])
        entryCbx2 = self.entryMaker([650, 280])
        entryCbx = self.entryMaker([650, 360])
        entryCbconst = self.entryMaker([650, 440])
        self.CubicEntries = [entryCbx3, entryCbx2, entryCbx, entryCbconst]

        # create and place the 'Next' button
        self.savebutton.place(x=600, y=500)
        pass


    def Quartic(self):
        # create labels for each coefficient
        self.labelMaker('x⁴',[550, 200])
        self.labelMaker('x³',[550, 270])
        self.labelMaker('x²',[550, 340])
        self.labelMaker('x',[550, 410])
        self.labelMaker('constant',[500, 480])
       
        # create entry fields for each coefficient and save them
        entryQtx4 = self.entryMaker([650, 200])
        entryQtx3 = self.entryMaker([650, 270])
        entryQtx2 = self.entryMaker([650, 340])
        entryQtx = self.entryMaker([650, 410])
        entryQtconst = self.entryMaker([650, 480])
        self.QuarticEntries = [entryQtx4, entryQtx3, entryQtx2, entryQtx, entryQtconst]

        # create and place the 'Next' button
        self.savebutton.place(x=600, y=550)
        pass


    def getData(self):
        # get reference to master
        master = self.master
        # initialize data to 'x' as placeholders
        master.data = ['x', 'x', 'x', 'x', 'x']
        # flag to check if data is valid or not
        flag = 0

        if(master.eqMode == 0):  # Quadratic
            for i in range(3):
                # get data from QuadraticEntries
                master.data[i] = self.QuadEntries[i].get()
                # check if data is valid
                if (('-' not in master.data[i]) and (master.data[i] == '' or not master.data[i].isnumeric())):
                    flag = 1

        if(master.eqMode == 1):  # Cubic
            for i in range(4):
                # get data from CubicEntries
                master.data[i] = self.CubicEntries[i].get()
                # check if data is valid
                if (('-' not in master.data[i]) and (master.data[i] == '' or not master.data[i].isnumeric())):
                    flag = 1

        if(master.eqMode == 2):  # Quartic
            for i in range(5):
                # get data from QuarticEntries
                master.data[i] = self.QuarticEntries[i].get()
                # check if data is valid
                if (('-' not in master.data[i]) and (master.data[i] == '' or not master.data[i].isnumeric())):
                    flag = 1

        if(flag == 1):
            # if data is invalid, show error message
            self.errorSc()
        else:
            # if data is valid, proceed to next screen
            master.optionSc()


    def errorSc(self):
        # get reference to master
        master = self.master
        # create label with error message
        label = Label(self.master.Frames[1], text='Invalid or Incomplete Data', font='Arial 18 bold italic')
        label.config(bg=master.primary[master.mode], fg='red')
        label.place(x=900, y=300)
        # destroy label after 1 second
        self.master.root.after(1000, label.destroy)
        