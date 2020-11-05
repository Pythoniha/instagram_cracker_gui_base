import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.geometry('400x300')
root.title('Instagram Cracker | GUI Base')




class single:
    def openfile():
        filedialog.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
        
        
    def single():
        global tex
        tex = tk.Label(root, text='Singel Cracked Processing')
        global username_label
        username_label = tk.Label(root,text='Username :')
        global entry_
        entry_ = tk.Entry(root)
        global passowrd_label
        passowrd_label = tk.Label(root,text='Password File : ')
        global import_password
        import_password = tk.Button(root,text='Import Password File ...',command=single.openfile)
        global thread
        thread = tk.Label(root,text='Enter Treading Number :')
        global thread_
        thread_ = tk.Scale(root, from_=0, to=10,orient=HORIZONTAL)
        global proxy
        proxy = tk.Button(root,text='Proxy', command=single.openfile)
        
        tex.place(x=1,y=30)
        username_label.place(x=1,y=45)
        entry_.place(x=1,y=70)
        passowrd_label.place(x=1,y=95)
        import_password.place(x=1,y=130)
        thread.place(x=1,y=155)
        thread_.place(x=1,y=170)
        proxy.place(x=1, y=210)
        
class combo:    
    def combo():
        tex.destroy()
        tex.destroy()
        username_label.destroy()
        entry_.destroy()
        passowrd_label.destroy()
        import_password.destroy()
        thread.destroy()
        thread_.destroy()
        proxy.destroy()
        
        load_file_combo = tk.Button(root,text='Load Combo ',command = single.openfile)
        scale_thread = tk.Scale(root, from_=0, to=10,orient=HORIZONTAL)
        start = tk.Button(root,text='Start Attack')
        
        
        
        load_file_combo.place(x=1,y=30)
        scale_thread.place(x=1,y=55)
        start.place(x=1,y=130)
        
        
set_1 = tk.Button(root,text='Single Crack',command = single.single)
set_2 = tk.Button(root,text='Combo List',command = combo.combo)



set_1.place(x=1,y=1)
set_2.place(x=80,y=1)

root.mainloop()
