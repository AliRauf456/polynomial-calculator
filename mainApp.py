#importing neccesary libraries and files
from tkinter import *
from polynomials import PolynomialsFrames
from Backend import Solution

class Application():
    root = Tk()  # create a new tkinter window
    mode = 1  # Default mode: 0-light, 1-dark 
    topBarColor = ['#78aaad','#0f343b']  # colors for the top bar
    primary = ['#d6dbce','#40676e']  # primary color theme
    primaryfg = ['#202d2e','#b0e1eb']  # primary foreground color theme
    secondary = ['#69878a','#113036']  # secondary color theme
    buttons = ['#88a6a8','#19464f']  # color theme for buttons
    buttonsfg = ['black','white']  # foreground color for buttons
    Frames = [0,0,0,0,0,0]  # list to store the frames created
    eqMode = -1  # variable to store equation mode (default value)

    def __init__(self):
        self.HomeFn()  # call HomeFn function when Application class is initialized

    # Event Bindings for entering and leaving buttons
    #------------------------------------------------
    def enterEvent(self, e):
        e.widget.config(cursor='hand2', bg=self.secondary[self.mode])
        pass

    def leaveEvent(self, e):
        e.widget.config(cursor='arrow', bg=self.buttons[self.mode], fg=self.buttonsfg[self.mode])
        pass

    def ButtonEnt(self,e):
        e.widget.config(cursor='hand2')
        pass

    def ButtonLeave(self,e):
        e.widget.config(cursor='arrow')
        pass

    def changeMod(self):
        #Function to change the color mode of the application.
        self.mode = 1-self.mode  # toggle the mode
        for i in self.root.winfo_children():  # destroy all child elements of the tkinter window
            i.destroy()
        self.HomeFn()  # create new elements with updated color mode
    
    def HomeFn(self):
        #Function to create and configure the home page of the application.
        root = self.root
        self.width = root.winfo_screenwidth()  # get the width of the screen
        self.height = root.winfo_screenheight()  # get the height of the screen

        root.geometry('900x600+220+50')  # set the geometry of the tkinter window
        root.state('zoomed')  # maximize the tkinter window
        root.title('Polynomial Calculator')  # set the title of the tkinter window

        topBar = Frame(root, width=self.width, height=50, bg=self.topBarColor[self.mode])  # create a new frame for the top bar
        topBar.pack()  # add the top bar to the tkinter window
        topBar.pack_propagate(False)  # prevent the frame from resizing

        for i in range(6):
            frame = Frame(root, height=self.height, width=self.width, bg=self.primary[self.mode])  # create a new frame
            frame.place(x=0, y=50)  # position the frame
            self.Frames[i] = frame  # add the frame to the Frames list
        
        self.PolynomialSc()  # call the PolynomialSc function to create the polynomial screen
        pass


    # Creates a label widget with given text, width, height, and font, and sets the background and foreground colors based on the current mode
    def LabelMaker(self, text, master, coord, width=20):
        label = Label(master, text=text, width=width, height=6, font='Arial 16 bold')
        label.config(bg=self.buttons[self.mode], fg=self.buttonsfg[self.mode])
        label.place(x=coord[0], y=coord[1], anchor='nw')
        return label

    # Clears the first frame, raises it, and creates a mode changer button, a label prompting the user to choose a polynomial type, and labels for each type of polynomial
    def PolynomialSc(self):
        # Clear the first frame
        for i in self.Frames[0].winfo_children():
            i.destroy()

        # Raise the first frame
        self.Frames[0].tkraise()
        master = self.Frames[0]

        # Create a mode changer button
        modeText=['Dark','Light']
        modeChanger = Button(self.Frames[0], text=modeText[self.mode], font='Arial 12 bold')
        modeChanger.config(fg=self.buttonsfg[1-self.mode], bg=self.buttonsfg[self.mode], width=10, command=self.changeMod)
        modeChanger.place(x=1200, y=10)

        # Bind events to the mode changer button
        modeChanger.bind('<Enter>', self.ButtonEnt)
        modeChanger.bind('<Leave>', self.ButtonLeave)

        # Create a label prompting the user to choose a polynomial type
        choosePol = Label(master, text='Choose Polynomial Type', bg=self.primary[self.mode])
        choosePol.config(font='Arial 19 bold', fg=self.primaryfg[self.mode])
        choosePol.place(x=530, y=150, anchor='nw')

        # Create labels for each type of polynomial
        quadratic = self.LabelMaker('Quadratic', master, [250,250])
        cubic = self.LabelMaker('Cubic', master, [550,250])
        quartic = self.LabelMaker('Quartic', master, [850,250])
        self.polynomialChoices = [quadratic, cubic, quartic]

        # Bind events to each polynomial label
        for i in self.polynomialChoices:
            i.bind('<Enter>', self.enterEvent)
            i.bind('<Leave>', self.leaveEvent)
            i.bind('<Button>', self.polynomialsChosen)


    # When a polynomial label is chosen, stores the chosen polynomial type and clears the second frame, then creates a back button and a frame for displaying the chosen polynomial
    def polynomialsChosen(self, e):
        if e != 1:
            self.idx = e.widget['text']

        # Clear the second frame
        for i in self.Frames[1].winfo_children():
            i.destroy()
        
        # Create a back button
        self.backBtn = Button(self.Frames[1], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
        self.backBtn.config(width=10, height=2, command=self.PolynomialSc)
        self.backBtn.place(x=40, y=30)
        
        # Create a frame for displaying the chosen polynomial
        PolynomialsFrames(self.idx, self)
        self.Frames[1].tkraise()


    def optionSc(self):
    # Loop through all children of the third frame and destroy them
        for i in self.Frames[2].winfo_children():
            i.destroy()

        # Create a back button on the third frame and configure it
        self.backBtn = Button(self.Frames[2], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
        self.backBtn.config(width=10, height=2, command=lambda:self.polynomialsChosen(1))
        self.backBtn.place(x=40, y=30)

        # Set the master to the third frame and raise it
        master = self.Frames[2]
        self.Frames[2].tkraise()

        # Create a label for choosing an option, configure it, and place it on the third frame
        label = Label(master, text='Choose Option', bg=self.primary[self.mode])
        label.config(fg=self.primaryfg[self.mode], font='Arial 14 bold')
        label.place(x=600, y=100)

        # Create labels for the different options, bind events to them, and add them to the optionList
        solve = self.LabelMaker('Solve', master, [200,250],17)
        differentiate = self.LabelMaker('Differentiate', master, [450,250],17)
        integrate = self.LabelMaker('Integrate', master, [700,250],17)
        graph = self.LabelMaker('Graph', master, [950,250],17)
        self.optionList = [solve, differentiate, integrate, graph]
        for i in self.optionList:
            i.bind('<Enter>', self.enterEvent)  # Bind enter event to enterEvent method
            i.bind('<Leave>', self.leaveEvent)  # Bind leave event to leaveEvent method
            i.bind('<Button>', self.optionsChosen)  # Bind button event to optionsChosen method


    
    def optionsChosen(self, e):
    # If the user didn't choose option 1 or 2, set idx2 to the text of the chosen option widget
        if e!=1 and e!=2:
            self.idx2 = e.widget['text']
      # If the user chose option 2 or 'Integrate':
        if self.idx2 == 'Integrate' or e == 2:
            # Switch to the fourth frame
            self.Frames[4].tkraise()
            
            # Create a back button in the fourth frame
            backBtn = Button(master=self.Frames[4], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
            backBtn.config(width=10, height=2, command=self.optionSc)
            backBtn.place(x=40, y=30)

            # Create labels for definite and indefinite integrals in the fourth frame
            DefiniteIntegral = self.LabelMaker('Definite Integral', self.Frames[4], [400,250])
            IndefiniteIntegral = self.LabelMaker('Indefinite Integral', self.Frames[4], [700,250])

            # Create a list of the integral labels and bind them to events
            self.IntegralList = [DefiniteIntegral, IndefiniteIntegral]
            for i in self.IntegralList:
                i.bind('<Enter>', self.enterEvent)
                i.bind('<Leave>', self.leaveEvent)
                
            # Set integralData to 1 and bind the labels to functions that handle clicks
            self.integralData = 1
            DefiniteIntegral.bind('<Button>', self.DefiniteIntegralsSc)
            IndefiniteIntegral.bind('<Button>', self.indefiniteIntegralSc)
            
        # If the user didn't choose option 2 or 'Integrate':
        else:
            # Destroy all widgets in the third frame
            for i in self.Frames[3].winfo_children():
                i.destroy()
            
            # Create a back button in the third frame
            self.backBtn = Button(self.Frames[3], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
            self.backBtn.config(width=10, height=2, command=self.optionSc)
            self.backBtn.place(x=40, y=30)
            
            # Call the Solution function with the chosen option, self, and the fourth frame
            Solution(self.idx2, self, self.Frames[4])
            
            # Switch to the third frame
            self.Frames[3].tkraise()

    
    def indefiniteIntegralSc(self, e):
    # Clear any children widgets present in the third frame
        for i in self.Frames[3].winfo_children():
            i.destroy()

        # Create a back button and place it in the third frame
        self.backBtn = Button(self.Frames[3], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
        self.backBtn.config(width=10, height=2, command=lambda:self.optionsChosen(2))
        self.backBtn.place(x=40, y=30)

        # Create a solution for the selected option and raise the third frame
        Solution(self.idx2, self, self.Frames[4], self.integralData)
        self.Frames[3].tkraise()        


    def DefiniteIntegralsSc(self, e):
        # Set the master window as the fifth frame
        master = self.Frames[5]
        # Raise the fifth frame
        self.Frames[5].tkraise()

        # Create a back button and place it in the fifth frame
        self.backBtn = Button(master, text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
        self.backBtn.config(width=10, height=2, command=self.optionSc)
        self.backBtn.place(x=40, y=30)

        # Create a label for entering the limits of the definite integral and place it in the fifth frame
        limits = Label(master, text='Enter Limits for Definite Integral', bg=self.primary[self.mode])
        limits.config(font='Arial 19 bold', fg=self.primaryfg[self.mode])
        limits.place(x=500, y=130, anchor='nw')

        # Create a label for the lower limit of the definite integral and place it in the fifth frame
        lowerLimit = Label(master, text='Lower Limit', bg=self.primary[self.mode])
        lowerLimit.config(font='Arial 19 bold', fg=self.primaryfg[self.mode])
        lowerLimit.place(x=500, y=250, anchor='nw')

        # Create a label for the upper limit of the definite integral and place it in the fifth frame
        upperLimit = Label(master, text='Upper Limit', bg=self.primary[self.mode])
        upperLimit.config(font='Arial 19 bold', fg=self.primaryfg[self.mode])
        upperLimit.place(x=500, y=350, anchor='nw')

        # Create an entry box for the lower limit and place it in the fifth frame
        self.lowerEntry = Entry(master, font='Arial 20 bold', width=10)
        self.lowerEntry.place(x=700, y=250)

        # Create an entry box for the upper limit and place it in the fifth frame
        self.upperEntry = Entry(master, font='Arial 20 bold', width=10)
        self.upperEntry.place(x=700, y=350)

        # Create a button to save the limits and proceed to the next step, and place it in the fifth frame
        self.savebutton = Button(master, text='Next', bg='#0c6375', fg='white')
        self.savebutton.config(height=2, width=14, font='Arial 14 bold', command=self.getData)
        self.savebutton.place(x=600, y=450)
        pass


    def getData(self):
        # Retrieve input values from user
        upperLimit = self.upperEntry.get()
        LowerLimit = self.lowerEntry.get()

        # Check if input values are valid
        if (('-' not in upperLimit) and (upperLimit == '' or not upperLimit.isnumeric())):
            self.errorSc()

        elif (('-' not in LowerLimit) and (LowerLimit == '' or not LowerLimit.isnumeric())):
            self.errorSc()
            
        # If input values are valid
        else:
            # Store input values in list
            self.integralData = [upperLimit, LowerLimit]

            # Clear the current frame
            for i in self.Frames[3].winfo_children():
                i.destroy()

            # Add back button to navigate back
            self.backBtn = Button(self.Frames[3], text='Back', bg='#0c6375', fg='white', font='Arial 12 bold')
            self.backBtn.config(width=10, height=2, command=lambda:self.optionsChosen(2))
            self.backBtn.place(x=40, y=30)

            # Generate solution
            Solution(self.idx2, self, self.Frames[4], self.integralData)
            self.Frames[3].tkraise()


    def errorSc(self):
        master = self.Frames[5]
        label = Label(master, text='Invalid or Incomplete Data', font='Arial 18 bold italic')
        label.config(bg=self.primary[self.mode], fg='red')
        label.place(x=900, y=300)

        # Destroy error message after 1 second
        self.root.after(1000, label.destroy)


app = Application()
app.root.mainloop()