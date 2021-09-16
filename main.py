from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        File = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()



def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad", "Notepad by Lokesh Vyas")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.geometry("380x206")
    root.title("Notepad By Lokesh Vyas")
    root.wm_iconbitmap("icon.ico")

    #Add TextArea
    TextArea = Text(root, font="Lucida 13")
    TextArea.pack(fill=BOTH, expand=True)
    file = None

    #Menu Bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    #File Menu Starts
    #To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    #To Save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()

    # To exit the notepad
    FileMenu.add_command(label="Exit", command = quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # Edit Menu Ends

    # Help MEnu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help MEnu Ends


    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()