from tkinter import *

window = Tk()

# window properties
window.title("PyCalc")
window.resizable(0,0)
window.configure(bg = '#000000')

# equation initialized as variable string
input = StringVar()
equation = ""

# calulation functions
def buttonPress(num):
	global equation
	equation += str(num)
	input.set(equation)
	
def evaluate():
	global equation
	total = eval(equation)
	input.set(total)
	equation = ""
	
def clear():
	global equation
	equation = ""
	input.set(equation)

# input field	
inputField = Label(window, relief = "groove", textvariable = input, height = 2, bg = "#cccccc", fg = "#000000")
inputField.grid(row = 0, column = 0, columnspan = 4, sticky=W+E)

# numrical buttons
button7 = Button(window, text = "7", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(7))
button7.grid(row = 1, column = 0, padx = 4, pady = 4)
button8= Button(window, text = "8", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(8))
button8.grid(row = 1, column = 1, padx = 4, pady = 4)
button9 = Button(window, text = "9", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(9))
button9.grid(row = 1, column = 2, padx = 4, pady = 4)
button4 = Button(window, text = "4", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(4))
button4.grid(row = 2, column = 0, padx = 4, pady = 4)
button5 = Button(window, text = "5", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(5))
button5.grid(row = 2, column = 1, padx = 4, pady = 4)
button6 = Button(window, text = "6", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(6))
button6.grid(row = 2, column = 2, padx = 4, pady = 4)
button1 = Button(window, text = "1", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(1))
button1.grid(row = 3, column = 0, padx = 4, pady = 4)
button2 = Button(window, text = "2", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(2))
button2.grid(row = 3, column = 1, padx = 4, pady = 4)
button3 = Button(window, text = "3", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(3))
button3.grid(row = 3, column = 2, padx = 4, pady = 4)
button0 = Button(window, text = "0", width = 6, height = 2, bg = "#606060", fg = "#FFFFFF", command = lambda:buttonPress(0))
button0.grid(row = 4, column = 1, padx = 4, pady = 4)

# functional buttons
buttonAdd = Button(window, text = "+", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = lambda:buttonPress("+"))
buttonAdd.grid(row = 1, column = 3, padx = 4, pady = 4)
buttonSub = Button(window, text = "-", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = lambda:buttonPress("-"))
buttonSub.grid(row = 2, column = 3, padx = 4, pady = 4)
buttonMul = Button(window, text = "*", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = lambda:buttonPress("*"))
buttonMul.grid(row = 3, column = 3, padx = 4, pady = 4)
buttonDiv = Button(window, text = "/", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = lambda:buttonPress("/"))
buttonDiv.grid(row = 4, column = 3, padx = 4, pady = 4)
buttonEqual = Button(window, text = "=", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = evaluate)
buttonEqual.grid(row = 4, column = 2, padx = 4, pady = 4)
buttonClear = Button(window, text = "C", width = 6, height = 2, bg = "#2b97f2", fg = "#FFFFFF", command = clear)
buttonClear.grid(row = 4, column = 0, padx = 4, pady = 4)

# infite loop to sustain window
window.mainloop()