from tkinter import *
from tkinter import messagebox, scrolledtext
import socket


from Activehosts import *



def showopenports(ipaddress):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    str = ""
    ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 143, 161, 194, 443]
    for port in ports:
        if s.connect_ex((ipaddress, port)):

            str += "[*] port {0} is closed\n".format(port)

        else:
            str += "[*] port {0} is open\n".format(port)
    Saveinfile.saveports(str)

    return str




def showactive():
    text.delete("1.0", END)
    clients=Activehosts.showalivedevices()

    for client in clients:
          text.insert(END,"ActiveHost --> "+client+".\n")
    text.insert(END,"\nfinish Scan!")

def showports():
    text.delete("1.0", END)
    messagebox.showinfo("important!!", "this option may take more than 10 seconds")

    ip = entry.get()
    str= showopenports(ip)
    text.insert(END,str)

def showhistory():
    text.delete("1.0",END)
    x=open("result.txt","r")
    text.insert(END,x.read())

def clear():
    text.delete("1.0",END)

def executecommand():
    text.delete("1.0",END)
    command = entry2.get()
    result=os.popen(command).read()
    text.insert(END,result)







window = Tk()
window.title("Network manager")
window.geometry("400x400")
window.iconbitmap("3123.ico")
window.resizable(False,False)
btn = Button(text ="press here to scan for active devices on your network", command=showactive)
btn.place(x=50,y=5)
label = Label(window,width="50",text="enter ip in this input for port scanning")
label.place(x=5,y=30)
entry = Entry(window,width="50")
entry.place(x=5,y=50)
text=scrolledtext.ScrolledText(window,wrap = WORD,width = 40,height = 10, font = ("Times New Roman", 15))
btn = Button(text ="show results history!", command=showhistory)
btn.place(x=30,y=130)
btn1 = Button(text ="clear", command=clear)
btn1.place(x=350,y=130)
label2 = Label(window)
label2.place(x=20,y=130)
entry2 = Entry(window,width="50")
entry2.place(x=5,y=100)
label3=Label(window,text="enter command to execute here")
label3.place(x=80,y=75)

btn2 = Button(text ="execute", command=executecommand)
btn2.place(x=330,y=98)

text.place(x=0,y=170)
btn1 = Button(text ="scan for ports", command=showports)
btn1.place(x=310,y=48)
window.mainloop()











