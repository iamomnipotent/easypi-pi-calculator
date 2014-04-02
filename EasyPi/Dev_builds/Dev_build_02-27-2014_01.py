# EasyPi Calculator Dev Build 02-27-2014
# Licensed under BSD License, GUI functions enabled by EasyGUI


# import files as needed
from decimal import *
import easygui as eg
import sys
import datetime


# main algorithm code branch

# main factorial function
def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

# main Plouff algorithm function
def plouff(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k = k + 1
    return pi

# main bellard algorithm function
def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
        k = k + 1
    pi = pi * 1/(2**6)
    return pi

# main chudnovsky algorithm function
def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k = k + 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


# main GUI code branch

# Startup confirmation window
firstLaunchMsg = "Welcome to EasyPi Calculator Dev Build 02-27-2014! Please make sure that you are running this application with administration rights. Press continue to continue to main program, or cancel to exit the program."
firstLaunchTitle = "EasyPi Calculator Startup"

if eg.ccbox(firstLaunchMsg, firstLaunchTitle):
    pass        # continue if the user chooses to
else:           # Exit the program if the user clicks on cancel
    sys.exit(0)

# use msgbox to display relative program information for the user
eg.msgbox("This program utilizes EasyGUI for the User Interface, and three different algorithms that include Plouff, Bellard and Chudnovsky.", "About this program")

# use msgbox to display critical information for the user
eg.msgbox("WARNING! When numbers are flashing in the console, it means that your CPU is working hard calculating Pi for you! Do not close the window until it's done, and the results will be displayed in the GUI again!", "WARNING - WARNING - WARNING")

# use integerbox to get user input for digits after the dot and iteration times
digitMsg = "Enter the digits after dot you want the program to calculate. Please enter a VALID INTEGER larger or equal to 0 and smaller or equal to 1000. Default is 10."
digitTitle = "Digits after dot"
digitDefault = 10
digitLowerBound = 0
digitUpperBound = 1000

# the input of integerbox is passed to a variable named digitAfterDot
digitAfterDot = eg.integerbox(digitMsg, digitTitle, digitDefault, digitLowerBound, digitUpperBound)

# set the number of digits after dot
getcontext().prec = digitAfterDot

# use another integerbox to get the number of iterations
iterationMsg = "Almost done! How many times do you want the program to calculate Pi? Please enter a VALID INTEGER larger or equal to 0 and smaller or equal to 999. Default is 25. WARNING: Some older computers might not be able to calculate all the way to iteration number 999!"
iterationTitle = "Iteration"
iterationDefault = 25
iterationLowerBound = 0
iterationUpperBound = 999

# the input of integerbox is passed to a variable named iterationNum
iterationNum = eg.integerbox(iterationMsg, iterationTitle, iterationDefault, iterationLowerBound, iterationUpperBound)

# output console message to file
class consoleLogger(object):

    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

# use datetime to determine name of results.txt
current_time = datetime.datetime.now()
current_time = current_time.replace(microsecond = 0)
resultFileName = "results.txt"

# main results code branch
sys.stdout = consoleLogger(resultFileName)
result_list = ['here are your results:', '\n']
for i in xrange(1,iterationNum+1):
    print "Iteration number ",i, plouff(i), bellard(i), chudnovsky(i)                           # print the results in the console
    results = "Iteration number ",str(i), str(plouff(i)), str(bellard(i)), str(chudnovsky(i))   # pass results into 'results' variable to be ready to passed into the list
    result_list.append(str(results) + '\n')                                                                 # pass results into the list

# use text to display results
eg.textbox("here are your results:", "results", result_list, 0)
