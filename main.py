from tkinter import *
import tkinter.font as font

def clearAll():
	result.config(text="")

def clearOne():
	try:
		text = str(result.cget("text"))
		text = text.replace(text[-1],"", 1)
		result.config(text=text)
	except:
		pass

def addNumber(text1):
	resultText = str(result.cget("text"))
	if len(resultText) <= 25:
		result.config(text=resultText+str(text1))

def addChar(text1):
	resultText = str(result.cget("text"))
	if len(resultText) <= 25:
		try:
			if text1 == '-' or text1 == '+' or text1 == '*' or text1 == '/' or text1 == '.':
				if resultText[-1] != '-' and resultText[-1] != '+' and resultText[-1] != '*' and resultText[-1] != '/' and resultText[-1] != '.':
					result.config(text=resultText+str(text1))
		except:
			pass
		
def calculate():
	try:
	    result.config(text=eval(result.cget("text")))  

	    calculation = str(result.cget("text"))
	    errorLabel.config(text="")  
	    if (str(calculation[-2:3]) == ".0"): 
	    	calculation = calculation.replace(calculation[-1],"", 1)
	    	calculation = calculation.replace(calculation[-1],"", 1)
	    	result.config(text=calculation)	
	except SyntaxError:
		errorLabel.config(text="SyntaxError") 
	except TypeError:
		errorLabel.config(text="TypeError")  

window = Tk()
window.title('Calculator')
#window.geometry("350x600")

BUTTOM_WIDTH = 5
BUTTOM_HEIGHT = 3
FONT = font.Font(size=16)

result = Label(window, height=3, font=font.Font(size=12))
result.grid(columnspan=11, rowspan=2,row=0,sticky='E')
buttonClearAll = Button(window, text="AC", font=font.Font(size=10), width=2, height=1, command=lambda: clearAll()).grid(columnspan=2, rowspan=1, column=1,row=0)
buttonClear = Button(window, text="CE", font=font.Font(size=10), width=2, height=1, command=lambda: clearOne()).grid(columnspan=2, rowspan=1, column=1,row=1)

button1 = Button(window, text="1", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(1)).grid(columnspan=2, rowspan=2, column=2,row=2)
button2 = Button(window, text="2", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(2)).grid(columnspan=2, rowspan=2, column=4,row=2)
button3 = Button(window, text="3", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(3)).grid(columnspan=2, rowspan=2, column=6,row=2)
buttonDivide = Button(window, text="/", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addChar("/")).grid(columnspan=2, rowspan=2, column=8, row=2)

button4 = Button(window, text="4", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(4)).grid(columnspan=2, rowspan=2, column=2,row=4)
button5 = Button(window, text="5", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(5)).grid(columnspan=2, rowspan=2, column=4,row=4)
button6 = Button(window, text="6", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(6)).grid(columnspan=2, rowspan=2, column=6,row=4)
buttonMultiply = Button(window, text="*", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addChar("*")).grid(columnspan=2, rowspan=2, column=8,row=4)

button7 = Button(window, text="7", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(7)).grid(columnspan=2, rowspan=2, column=2,row=8)
button8 = Button(window, text="8", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(8)).grid(columnspan=2, rowspan=2, column=4,row=8)
button9 = Button(window, text="9", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber(9)).grid(columnspan=2, rowspan=2, column=6,row=8)
buttonSubtract = Button(window, text="-", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addChar("-")).grid(columnspan=2, rowspan=2, column=8,row=8)

button0 = Button(window, text="0", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addNumber("0")).grid(columnspan=2, rowspan=2, column=2,row=10)
buttonComma = Button(window, text=",", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addChar(".")).grid(columnspan=2, rowspan=2, column=4,row=10)
buttonCalculate = Button(window, text="=", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: calculate()).grid(columnspan=2, rowspan=2, column=6,row=10)
buttonAdd = Button(window, text="+", font=FONT, width=BUTTOM_WIDTH, height=BUTTOM_HEIGHT, command=lambda: addChar("+")).grid(columnspan=2, rowspan=2, column=8,row=10)

errorLabel = Label(window, text="", height=1, fg="red", font=font.Font(size=12))
errorLabel.grid(columnspan=11, rowspan=1,row=12, sticky='S', pady=5)


window.resizable(False, False)
window.mainloop()