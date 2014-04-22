import Tkinter

class simpleapp_tk(Tkinter.Tk): #inherit from Tkinter.Tk the base class for windows
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)/