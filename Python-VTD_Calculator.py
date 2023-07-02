from tkinter import *
root = Tk()
root.title("VTD Calculator")

#estilos
root.configure(background='white')
display_style = {'background': 'white', 'foreground': 'black', 'font':("arial", 14)}
label_style = {'background': 'white', 'foreground': 'black', 'font':("arial", 12)}
button_style = {'background': 'lightgray', 'foreground': 'black', 'font':("arial", 12), 'width':5}

#funciones
def solve():
    try:
        valor_v=float(displayV.get())
        valor_t=float(displayT.get())
        valor_d=float(displayD.get())
        if valor_v==0:
            result = valor_d/valor_t
            displayR.delete(0,END)
            displayR.insert(0, result)
        if valor_d==0:
            result = valor_v*valor_t            
            displayR.delete(0,END)
            displayR.insert(0, result) 
        if valor_t==0:
            result = valor_d/valor_v
            displayR.delete(0,END)
            displayR.insert(0, result)
    except ValueError:
            displayR.delete(0,END)
            displayR.insert(0, "Error")

def clear_display():
    displayR.delete(0, END)
#texto
labelmsg=Label(root, text="Enter a value of 0, in the box corresponding to the unknown",**label_style)
labelV = Label(root, text="Velocity:", **label_style)
labelT = Label(root, text="Time:", **label_style)
labelD = Label(root, text="Distance:", **label_style)
labelR = Label(root, text="Result:", **label_style)
#posicion texto
labelmsg.grid(row=0,column=0,columnspan=5,sticky=W+E)
labelV.grid(row=1,column=0,sticky=W+E)
labelT.grid(row=2,column=0,sticky=W+E)
labelD.grid(row=3,column=0,sticky=W+E)
labelR.grid(row=4,column=0,sticky=W+E)

#entrada
displayV = Entry(root,display_style)
displayT = Entry(root,display_style)
displayD = Entry(root,display_style)
displayR = Entry(root,display_style)
#posicion entrada
displayV.grid(row=1,column=1,columnspan=5,sticky=W+E)
displayT.grid(row=2,column=1,columnspan=5,sticky=W+E)
displayD.grid(row=3,column=1,columnspan=5,sticky=W+E)
displayR.grid(row=4,column=1,columnspan=6,sticky=W+E)

#botones
Button(root, text='Solve',command=lambda:solve(),**button_style).grid(rowspan=3,row=1,column=7,columnspan=4,sticky=N+S)
Button(root, text='Clear',command=lambda:clear_display(),**button_style).grid(row=4,column=7)

root.mainloop()