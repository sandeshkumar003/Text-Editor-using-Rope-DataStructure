from tkinter import *
from tkinter import filedialog 
from tkinter import font 

class TextEditor:

    def __init__(self,root) :
        self.root = root

        self.root.title ("Text Editor using Rope Data Structure")

        self.root.geometry("1200x660")

        self.filename = None
        
        self.title = StringVar() #Title variable

        self.status = StringVar() #Status Variable

        #Text Pad working
        self.titlebar = Label(self.root,textvariable=self.title,font= ("Helvetica",16,"bold"),relief=GROOVE)
        self.titlebar.pack(side=TOP,fill=Y)
        self.settitle()

         # Creating Statusbar
        self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15),relief=GROOVE)
        self.statusbar.pack(side=BOTTOM,fill=BOTH)
        self.status.set("Welcome To Text Editor")
       
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root)
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",12),selectbackground="yellow", selectforeground="Red", undo= True)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=50)

        #Creating Menu:
        self.menubar = Menu(self.root,font=("times new roman",15),activebackground="Yellow")
        self.root.config(menu=self.menubar)

        # Creating File Menu
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
        self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
        self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)


        #Edit menu:
        self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.editmenu)

        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.filemenu.add_separator()
        # self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)

        # #self.editmenu.add_command(label="Redo")
        


    # # Adding New file Command
    #     
    # # Adding Open file Command
    #     




    def settitle(self):
        if self.filename:
         # Updating Title as filename
            self.title.set(self.filename)
        else:
             # Updating Title 
            self.title.set("TEXT PAD")
    
    def newfile(self,*args):
        self.txtarea.delete("1.0",END)  # Clear Area first
        self.filename = None   #New File as None
        self.settitle()
        self.status.set("New File Created") #Status created form welcome to editor to new file created

    def openfile(self,*args):
    # Exception handling
        try:
            self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename != None:
                infile = open(self.filename,"r") #read mode
                self.txtarea.delete("1.0",END)  # Clearing text area
                for line in infile:   # Inserting data into text area
                    self.txtarea.insert(END,line)
                infile.close()
                self.settitle()
                self.status.set("Opened Successfully") #status changed!
        except Exception as e:
                messagebox.showerror("Exception",e)

    def savefile(self,*args):

        try:
            if self.filename != None:
                data = self.txtarea.get("1.0",END) #reading the file
                outfile = open(self.filename,"w")  # opening File in write mode
                outfile.write(data)
                outfile.close()
                self.settitle()
                self.status.set("Saved Successfully") #status changed
            # else:
            #     self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception",e)

    def exit(self,*args):
        op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
        if op>0:
            self.root.destroy()
        else:
            return
    
    def cut(self,*args):
        self.txtarea.event_generate("<<Cut>>")

    def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")
 
    def paste(self,*args):
        self.txtarea.event_generate("<<Paste>>")

    

root = Tk()
TextEditor(root)
root.mainloop()