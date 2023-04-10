from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
root=Tk()
root.title("Planet Encyclopedia")
root.geometry("600x600")
root.configure(background="aquamarine")
pi=Label(root,font=("Comic Sans MS",18,"bold"),bg="aquamarine")
pi.pack()
img_path=""
def Openimage():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Text File ",
    filetypes=[("Image file","*.jpg;*.gif;*.jpg;;*.png;*.txt",)])
    print(img_path)
    img_e=ImageTk.PhotoImage(f)
    pl["image"]=f
    f.close()
def ri():
    global img_path
    img=Image.open(f)
    r=f.rotate(180)
    img=ImageTk.PhotoImage(r.rotate(180))
bt=Button(root,text="Rotate",command=ri) 
bt.pack()   
btn=Button(root,text="Open Image",command=Openimage)
btn.pack()
root.mainloop()
    
    
