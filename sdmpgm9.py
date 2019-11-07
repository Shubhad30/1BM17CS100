from tkinter import *
def f1():
    print("gvfg")


root=Tk()
root.title("online movie")
root.geometry("500x500+600+300")
l1=Label(root,text="enter the languge:")
l1.grid(row=0,column=0,columnspan=3)
cv1=BooleanVar()
c1=Checkbutton(root,text="English",variable=cv1,command=f1)
c1.grid(row=1,column=0)
cv2=BooleanVar()
c2=Checkbutton(root,text="Hindi",variable=cv2,command=f1)
c2.grid(row=2,column=0)
cv3=BooleanVar()
c3=Checkbutton(root,text="Kannada",variable=cv3,command=f1)
c3.grid(row=3,column=0)

root.mainloop()
