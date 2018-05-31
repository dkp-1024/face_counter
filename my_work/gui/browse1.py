from tkinter import filedialog
from tkinter import Tk
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)