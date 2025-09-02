import tkinter as tkt
calculation = ""
def add_to_calculation(sym):
    global calculation
    calculation += str(sym)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculator():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear()
        text_result.insert(1.0,"Error")

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

#Size of the calculator:
root = tkt.Tk()
root.geometry("300x275")

text_result = tkt.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

button_1 = tkt.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
button_1.grid(row=2, column=1)
button_2 = tkt.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=2)
button_3 = tkt.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=3)
button_4 = tkt.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=1)
button_5 = tkt.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=2)      
button_6 = tkt.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=3)
button_7 = tkt.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=1)  
button_8 = tkt.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=2)  
button_9 = tkt.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=3)
button_0 = tkt.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=2)
button_plus = tkt.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)   
button_minus = tkt.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)  
button_multiply = tkt.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
button_multiply.grid(row=4, column=4)
button_divide = tkt.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
button_divide.grid(row=5, column=4)
button_open = tkt.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
button_open.grid(row=5, column=1)
button_close = tkt.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
button_close.grid(row=5, column=3)
button_equals = tkt.Button(root, text="=", command=evaluate_calculator, width=11, font=("Arial", 14))
button_equals.grid(row=6, column=1, columnspan=2)
button_clear = tkt.Button(root, text="C", command=clear, width=11, font=("Arial", 14))
button_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()





