from tkinter import *
def hello():
    print("welcome to python")
root= Tk()
root.geometry("655x333")
f2= Frame(root,bg="gray", borderwidth=3,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
b1= Button(f2,text="button",command=hello, fg="white",bg="black")
b1.pack(side=LEFT,padx=5)
b2= Button(f2,text="button",command=hello, fg="white",bg="black")
b2.pack(side=LEFT,padx=5)
b3= Button(f2,text="button",command=hello, fg="white",bg="black")
b3.pack(side=LEFT,padx=5)
root.mainloop() 