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
		self.entryVariable.set(u"Enter Text Here.")
		
		button = Tkinter.Button(self, text=u"Click me !", command=self.OnButtonClick) #create button
		button.grid(column=1,row=0) #add button to grid
		
		self.labelVariable = Tkinter.StringVar()
		label =Tkinter.Label(self,textvariable=self.labelVariable, anchor="w" ,fg="white" ,bg="blue") #create label
		label.grid(column=0,row=1,columnspan=2,sticky='EW') #add label to grid
		self.labelVariable.set(u"Hello!")
		
		self.grid_columnconfigure(0,weight=1) #widjets adjust to window size
		self.resizable(True,False) #limits the window to only resize horizontally
		self.update()
        self.geometry(self.geometry())       
		self.entry.focus_set()
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