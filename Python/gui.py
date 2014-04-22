import Tkinter

class simpleapp_tk(Tkinter.Tk): #inherit from Tkinter.Tk the base class for windows
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent #reference to parent
		self.initialise()
		
	def initialise(self): #method that will create everything like voidsetup etc
		pass
if __name__ == "__main__":
	app = simpleapp_tk(None) # instantiate the class, parent = none
	app.title('My Application') # window title
	app.mainloop() # loop indefinitely