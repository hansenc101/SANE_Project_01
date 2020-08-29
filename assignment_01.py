import sys
import random
from PyQt5 import QtWidgets,uic

Click_Count = 0

## ----------------------------------------------------------------------------
## Quit
##   
## Purpose:
##   Quits the application
##
## ----------------------------------------------------------------------------
def Quit():
    App.quit()

## ----------------------------------------------------------------------------
## Handle Click
##   
## Purpose:
##   Process the click event.  Increment the persistant click counter
##   and set the background of the label to a random color
##
## ----------------------------------------------------------------------------
def Handle_Click():
    global Click_Count
    Click_Count = Click_Count + 1

    BG_Color = "rgb(" + str(random.randint(0,255)) + "," + str(random.randint(0,255)) + "," + str(random.randint(0,255)) + ");"
    FG_Color = "rgb(255,255,255);" # white
    Green_Color = "rgb(0,255,0);" # color green
    Blue_Color = "rgb(0,0,255);" # color blue
    Yellow_Color = "rgb(255,255,0);" # color yellow
    Orange_Color = "rgb(255,124,0);" # color orange
    Red_Color = "rgb(255,0,0);" # color green


    #UI.lblOutput.setText("Clicked " + str(Click_Count) + " times")
    #UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")

    finalGrade = float(calcGrades())
    letterGrade = "F"
    BG_Color = Red_Color

    if finalGrade >= 89.5:
        letterGrade = "A"
        BG_Color = Green_Color
    elif finalGrade >= 79.5 and finalGrade < 89.5:
        letterGrade = "B"
        BG_Color = Blue_Color
    elif finalGrade >= 69.5 and finalGrade < 79.5:
        letterGrade = "C"
        BG_Color = Yellow_Color
        FG_Color = "rgb(0,0,0);"
    elif 59.5 <= finalGrade and finalGrade < 69.5:
        letterGrade = "D"
        BG_Color = Orange_Color
    elif finalGrade < 59.5:
        letterGrade = "F"
        BG_Color = Red_Color


    UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")
    UI.lblOutput.setText("Final Grade:  " + str(finalGrade) + "% - " + letterGrade)


## ----------------------------------------------------------------------------
## Calculate Grades
##   
## Purpose:
##   Calculate the final percentage for the course and return this value
##
## ----------------------------------------------------------------------------
def calcGrades():
    homeworkGrade = float(UI.homeworkGrade.text()) # homework grade input from gui; following declarations follow same approach
    homeworkGradePerc = 30 * (homeworkGrade/100) # weighted percentage; ; following declarations follow same approach

    assignmentsGrade = float(UI.assignmentsGrade.text())
    assignmentsGradePerc =  10 * (assignmentsGrade/100)

    exam01Grade = float(UI.exam01Grade.text())
    exam01GradePerc = 15 * (exam01Grade/100)

    midtermGrade = float(UI.midtermGrade.text())
    midtermGradePerc = 10 * (midtermGrade/100)
    
    exam02Grade = float(UI.exam02Grade.text())
    exam02GradePerc = 15 * (exam02Grade/100)

    finalProjectGrade = float(UI.finalGrade.text())
    finalProjectGradePerc = 20 * (finalProjectGrade/100)

    finalGradePerc = homeworkGradePerc + assignmentsGradePerc + exam01GradePerc + midtermGradePerc + exam02GradePerc + finalProjectGradePerc
    return finalGradePerc


    
## ----------------------------------------------------------------------------
## demo_gui
##   
## Purpose:
##   Provide a sample progarm to demonstrate basic Python and Qt interaction
##
## ----------------------------------------------------------------------------
App = QtWidgets.QApplication([])
UI=uic.loadUi("assignment_01.ui")

UI.btnCalculate.clicked.connect(Handle_Click)
UI.actionCalculate.triggered.connect(Handle_Click)
UI.actionQuit.triggered.connect(Quit)

UI.show()
sys.exit(App.exec_())