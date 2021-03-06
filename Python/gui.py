#
# First tutorial for GUI, modifying for requirements.
#
#

import Tkinter

class simpleapp_tk(Tkinter.Tk): #inherit from Tkinter.Tk the base class for windows
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent #reference to parent
		self.initialise()
		
	def initialise(self): #method that will create everything like voidsetup etc
		self.grid() #window mode assigns items to a grid
		
		self.entryVariable =Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable=self.entryVariable) # CREATE widget
		self.entry.grid(column=0,row=0, sticky='EW')#Add widget to the layout manager
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter Required Power (1-9)")
		
		button = Tkinter.Button(self, text=u"Update", command=self.OnButtonClick) #create button
		button.grid(column=1,row=0) #add button to grid
		
		
		#labels
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=0,row=1,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Power Out")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=1,row=1,columnspan=1,sticky='W') #add label to grid
		self.labelVariable.set(u"12345")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=2,row=1,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Watts")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=0,row=2,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Power Required")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=1,row=2,columnspan=1,sticky='W') #add label to grid
		self.labelVariable.set(u"12345")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=2,row=2,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Watts")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=0,row=3,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Voltage Out")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=1,row=3,columnspan=1,sticky='W') #add label to grid
		self.labelVariable.set(u"12345")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=2,row=3,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"Volts")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=0,row=4,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"PWM Duty Cycle")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=1,row=4,columnspan=1,sticky='W') #add label to grid
		self.labelVariable.set(u"1")
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="black") #create label
		label.grid(column=2,row=4,columnspan=1,sticky='E') #add label to grid
		self.labelVariable.set(u"%")
		
		#Layout Properties
		self.grid_columnconfigure(0,weight=1) #widjets adjust to window size
		self.resizable(True,False) #limits the window to only resize horizontally
		self.update()
		self.geometry(self.geometry())       
		self.entry.focus_set() #Unexpected indent
		self.entry.selection_range(0,Tkinter.END)
		
		
	def OnButtonClick(self):
		self.labelVariable.set(self.entryVariable.get()+"(You clicked thebutton!)")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
	
	def OnPressEnter(self,event):
		self.labelVariable.set(self.entryVariable.get()+"(You pressed enter !)")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
		
		
if __name__ == "__main__":
	app = simpleapp_tk(None) # instantiate the class, parent = none
	app.title('My Application') # window title
	app.mainloop() # loop indefinitely