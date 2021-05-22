from tkinter import *
from tkinter import filedialog 
from tkinter import font
from tkinter import messagebox
from Rope import *

######## from docx import Document
characters = 0
class TextEditor:


    def __init__(self,root) :
        self.root = root
        self.savecount = 0 #------------2

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
        self.filemenu.add_command(label="Save As",accelerator="Ctrl+Shift+S",command=self.saveasfile) #----------------- 1
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit)


        #Edit menu:
        self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.filemenu.add_separator()

        # self.editmenu.add_command(label="Undo",command=self.undo)

        # #self.editmenu.add_command(label="Redo")

        self.shortcuts() #---------------------- 3
        
##https://www.youtube.com/watch?v=UlQRXJWUNBA

##https://www.codespeedy.com/create-a-text-editor-in-python/ 



    def settitle(self):
        # if self.filename:
        #  # Updating Title as filename
        #     self.title.set("Text editor")
        # else:
             # Updating Title 
        self.title.set("TEXT PAD")
    
    def newfile(self,*args):
        self.txtarea.delete("1.0",END)  # Clear Area first
        self.filename = None   #New File as None
        self.settitle()
        self.status.set("New File Created") #Status created form welcome to editor to new file created
        self.savecount = 0

    def openfile(self,*args):
    # Exception handling
        try:
            self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename != None:
                infile = open(self.filename) #read mode
                
                self.txtarea.delete("1.0",END)  # Clearing text area
                counter = 0
                
                while True:
                            if counter > 11:
                                if counter % 6 == 0 :
                                    character = infile.read(6)
                                    if not character:
                                        break
                                    rope, characters = Rope.insertion(character, characters)
                                    self.txtarea.insert(END,character)
                                    print(character)
                            else :
                                character = infile.read(11)
                                if not character:
                                    break
                                rope,characters = add_first(character)
                            
                                self.txtarea.insert(END,character)
                                print(character)
                                return rope
 
                            counter +=1
                            
                            
                infile.close()
                self.settitle()
                self.status.set("Opened Successfully") #status changed!
        except Exception as e:
                print("Can't Access")

    def saveasfile(self,*args):
        
        # Exception handling
        try:
        # Asking for file name and type to save
            self.filename = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("Text Files","*.txt"),("Python Files","*.py")))
            # Reading the data from text area
            data = self.txtarea.get("1.0",END)
            # opening File in write mode
            outfile = open(self.filename,"w")
            # Writing Data into file
            outfile.write(data)
            # Closing File
            outfile.close()
            # Updating filename as Untitled
            # self.filename = untitledfile
            # Calling Set title
            self.settitle()
            # Updating Status
            self.status.set("Saved Successfully")
        except Exception as e:
            print("Can't access")
            # messagebox.showerror("Exception",e) ####### working ################
              # Defining Save As File Funtion


    def savefile(self,*args):

        try:
            if self.savecount != 0:
                if self.filename != None:
                    data = self.txtarea.get("1.0",END) #reading the file
                    outfile = open(self.filename,"w")  # opening File in write mode
                    outfile.write(data)
                    outfile.close()
                    self.settitle()
                    self.status.set("Saved Successfully") #status changed
                # else:
                #     self.saveasfile()
            elif self.savecount == 0:
                self.savecount +=1
                self.saveasfile()
            
        except Exception as e:
            print("Can't access")

   
    

    def exit(self,*args):
            self.root.destroy()
        
    
    def cut(self,*args):
        self.txtarea.event_generate("<<Cut>>")

    def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")
 
    def paste(self,*args):
        self.txtarea.event_generate("<<Paste>>")

    # Defining shortcuts Funtion
    def shortcuts(self,*args):
        # Binding Ctrl+n to newfile funtion
        self.txtarea.bind("<Control-n>",self.newfile)
        
        self.txtarea.bind("<Control-o>",self.openfile)
        
        self.txtarea.bind("<Control-s>",self.savefile)
        
        # self.txtarea.bind("<Control-a>",self.saveasfile)  # not working
        # Binding Ctrl+e to exit funtion
        self.txtarea.bind("<Control-e>",self.exit)
        
        #### have not added their funct yet ###########
        # self.txtarea.bind("<Control-x>",self.cut)
        # self.txtarea.bind("<Control-c>",self.copy)
        # self.txtarea.bind("<Control-v>",self.paste)

root = Tk()
TextEditor(root)
root.mainloop()