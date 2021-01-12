import re

print("This is a Simple Calculator.")
print("Type quit to exit programm!")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0: #first calculation
        equation = input("Enter Equation!")
    else: #following operations
        equation = input(str(previous))

    if equation == 'quit': #end programm
        print("Goodbye")
        run = False
    else: #calculate
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #filter out letters etc
        print(equation)
        previous = eval(equation)#do calculation

        print("You typed ", previous)

while run: # slope runs until run ist not True
    performMath()