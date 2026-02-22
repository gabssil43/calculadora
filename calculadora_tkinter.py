#PROJETO CALCULADORA EM PYTHON COM TKINTER

from tkinter import *
from tkinter import ttk

#cores
cor1 = "#8A4EBB" 
cor2= "#755491"
cor3 = "#9839E6" 
cor4= "#5B4D66"
cor5= "#38353C"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#frames
frame_Tela = Frame(janela, width=235, height=50, bg=cor2)
frame_Tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#botoes
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0) 
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=172, y=0)

# b_4 = Button(frame_corpo, text="7", width=11, height=2)
# b_4.place(x=80, y=0)
# b_5 = Button(frame_corpo, text="8", width=11, height=2)
# b_5.place(x=0, y=0)
# b_6 = Button(frame_corpo, text="9", width=11, height=2)
# b_6.place(x=80, y=0)
# b_7 = Button(frame_corpo, text="*", width=11, height=2)
# b_7.place(x=0, y=0)
# b_8 = Button(frame_corpo, text="4", width=11, height=2)
# b_8.place(x=80, y=0)
# b_9 = Button(frame_corpo, text="5", width=11, height=2)
# b_9.place(x=0, y=0) 
# b_10 = Button(frame_corpo, text="6", width=11, height=2)
# b_10.place(x=80, y=0)
# b_11 = Button(frame_corpo, text="-", width=11, height=2)
# b_11.place(x=0, y=0)
# b_12 = Button(frame_corpo, text="1", width=11, height=2)
# b_12.place(x=80, y=0)
# b_13 = Button(frame_corpo, text="2", width=11, height=2)
# b_13.place(x=0, y=0)
# b_14 = Button(frame_corpo, text="3", width=11, height=2)
# b_14.place(x=80, y=0)
# b_15 = Button(frame_corpo, text="+", width=11, height=2)
# b_15.place(x=0, y=0)
# b_16 = Button(frame_corpo, text="0", width=11, height=2)
# b_16.place(x=80, y=0)
# b_17 = Button(frame_corpo, text=".", width=11, height=2)
# b_17.place(x=0, y=0)
# b_18 = Button(frame_corpo, text="=", width=11, height=2)
# b_18.place(x=80, y=0)

janela.mainloop()