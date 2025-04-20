#importing neccesary libraries and files
from tkinter import *
import Calculator

class Solution:
    def __init__(self, idx, master, master2, integralData = -1):
        # Initialize the Solution class with necessary variables
        self.master = master
        self.master2 = master2
        self.iData = integralData
        data = master.data
        # Convert numerical data to integers if possible
        for i in range(len(data)):
            if data[i]!='x':
                data[i] = int(data[i])
        
        # Determine which function to call based on the given index
        if (idx == 'Solve'):
            self.solveFn(data)
        if (idx == 'Differentiate'):
            self.differentiateFn(data)
        if (idx == 'Integrate'):
            self.integrateFn(data)
        if (idx == 'Graph'):
            self.graphFn(data)
        
        # Create a button to allow user to calculate again
        calculateAgain = Button(master.Frames[3], text = 'Calculate Again', bg='#0c6375', fg='white')
        calculateAgain.config(font='Arial 14 bold', width=18, height=2, command=self.master.Frames[0].tkraise)
        calculateAgain.place(x=550, y=400)
        pass

    def solveFn(self, data):
        # Getting the master object
        master = self.master
        # If the equation mode is 0, solve quadratic equation using Calculator.Quadratic()
        if(master.eqMode == 0):
            result = Calculator.Quadratic(1, data[0], data[1], data[2])
        # If the equation mode is 1, solve cubic equation using Calculator.Cubic()
        if(master.eqMode == 1):
            result = Calculator.Cubic(1, data[0], data[1], data[2], data[3])
        # If the equation mode is 2, solve quartic equation using Calculator.Quartic()
        if(master.eqMode == 2):
            result = Calculator.Quartic(1, data[0], data[1], data[2], data[3], data[4])

        # Creating a label to display the result
        label = Label(master.Frames[3], text=result, bg=master.primary[master.mode], fg=master.primaryfg[master.mode])
        label.config(font='Arial 20 bold')
        label.place(x=670, y=250, anchor='center')
        pass

    
    def differentiateFn(self, data):
        # Getting the master object
        master = self.master
        # If the equation mode is 0, differentiate quadratic equation using Calculator.Quadratic()
        if(master.eqMode == 0):
            result = Calculator.Quadratic(2, data[0], data[1], data[2])
        # If the equation mode is 1, differentiate cubic equation using Calculator.Cubic()
        if(master.eqMode == 1):
            result = Calculator.Cubic(2, data[0], data[1], data[2], data[3])
        # If the equation mode is 2, differentiate quartic equation using Calculator.Quartic()
        if(master.eqMode == 2):
            result = Calculator.Quartic(2, data[0], data[1], data[2], data[3], data[4])

        # Creating a label to display the result
        label = Label(master.Frames[3], text=result, bg=master.primary[master.mode], fg=master.primaryfg[master.mode])
        label.config(font='Arial 20 bold')
        label.place(x=670, y=250, anchor='center')
        pass

    
    def integrateFn(self, data):
        # raise the second frame
        self.master2.tkraise()
        
        # determine the equation mode
        master = self.master
        if(master.eqMode == 0):
            if(self.iData == 1):
                # if there is one known point, integrate using it
                result = Calculator.Quadratic(3, data[0], data[1], data[2], 1)
            else:
                # if there are two known points, integrate between them
                result = Calculator.Quadratic(3, data[0], data[1], data[2], 2, self.iData[0], self.iData[1])
            
        if(master.eqMode == 1):
            if(self.iData == 1):    
                result = Calculator.Cubic(3, data[0], data[1], data[2], data[3], 1)
            else:
                result = Calculator.Cubic(3, data[0], data[1], data[2], data[3], 2, self.iData[0], self.iData[1])

        if(master.eqMode == 2):
            if(self.iData == 1):    
                result = Calculator.Quartic(3, data[0], data[1], data[2], data[3], data[4], 1)
            else:
                result = Calculator.Quartic(3, data[0], data[1], data[2], data[3], data[4], 2, self.iData[0], self.iData[1])
                
        # display the result
        label = Label(master.Frames[3], text = result, bg=master.primary[master.mode], fg=master.primaryfg[master.mode])
        label.config(font='Arial 20 bold')
        label.place(x=670, y=250, anchor='center')
        pass

    def graphFn(self, data):
        # determine the equation mode and graph the equation
        master = self.master
        
        if(master.eqMode == 0):
            Calculator.Quadratic(4, data[0], data[1], data[2])
        if(master.eqMode == 1):
            Calculator.Cubic(4, data[0], data[1], data[2], data[3])
        if(master.eqMode == 2):
            Calculator.Quartic(4, data[0], data[1], data[2], data[3], data[4])
        pass
   