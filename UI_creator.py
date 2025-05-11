from tkinter import filedialog, Tk, Button, Label

filepath = "" #path of the file

def get_file_path():
    return filepath #return the path of the file

def select_file():
    global filepath
    root = Tk()
    root.withdraw()
    root.update()
    path = filedialog.askopenfilename(
        title="Select Invoice PDF",
        initialdir=".",
        filetypes=[("PDF Files","*.pdf")]
    )
    root.destroy()

    if path:
        filepath = path
       
        
        
def ui_creator():
    ui= Tk()
    global filepath
    ui.title("PDF Reader") #title of the window
    ui.minsize(500,300) #minimum size of the window
    ui.maxsize(500,300) #maximum size of the window
    ui.update_idletasks() #update the window
    w = 500
    h = 300
    x = (ui.winfo_screenwidth() // 2) - (w // 2)
    y = (ui.winfo_screenheight() // 2) - (h // 2)
    ui.geometry(f"{w}x{h}+{x}+{y}")
    ui.config(bg="white") #background color of the window
    ui.resizable(0,0) #window is not resizable
    
    Label(text="Uplaod your PDF file",bg="white",fg="black",font=("Time New Roman",15,'bold')).pack(pady=50) #pack the label in the window

    Button(text="Upload",bg="black",fg="white",font=("Time New Roman",15,'bold'),command=select_file).pack(pady=0) #button to upload the file
    Button(text="Exit",bg="black",fg="white",font=("Time New Roman",15,'bold'),command=ui.quit).pack(pady=1) #button to exit the window
    
    ui.mainloop() #basic window
    



