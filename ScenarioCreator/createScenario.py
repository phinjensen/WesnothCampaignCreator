#IMPORTS!!!!!!! :D
import sys, os, tkFileDialog, tkMessageBox, Tkinter, ImageTk
from sideLib import *
from scenarioTemplate import *
from Tkinter import *
from ttk import *
scenarioMap = None

#Configure Tkinter and ttk
root = Tk()
root.title("Scenario Creator")
if sys.platform == "linux2":
    Theme = Style()
    Theme.theme_use('clam')

#Classes...
class team:
    """A class for the individual Sides."""
    def __init__(self, leaderName, Type, Canrecruit, Controller, SideNum, Gold, Income, Fog, Shroud, Team_name, Recruit):
        self.Id = leaderName.replace(' ', '_')
        self.SideVar = side.splitlines()
        self.SideVar[2] += Type
        self.SideVar[3] += '_ "' + leaderName + '"'
        self.SideVar[4] += self.Id 
        self.SideVar[5] += Canrecruit 
        self.SideVar[6] += "yes"
        self.SideVar[7] += Controller
        self.SideVar[8] += SideNum
        self.SideVar[9] += Gold + "}"
        self.SideVar[10] += Income
        self.SideVar[11] += Fog
        self.SideVar[12] += Shroud
        self.SideVar[13] += Team_name.replace(' ', '_')
        self.SideVar[14] += Team_name + '"'
        self.SideVar[15] += Recruit
        self.SideVar = "\n".join(self.SideVar)

#Funkshuns...
def getImageName(varName, entryName, issmallimage, canvasName, frame):
    varName = tkFileDialog.askopenfilename(filetypes=[("All files", "*"), ("PNG Images", "*.png")])
    entryName.insert(0, varName)
    if issmallimage:
        img = ImageTk.PhotoImage(file=varName)
        canvasName.delete(ALL)
        canvasName.create_image(2, 2, image=img, anchor=NW)
        canvasName.config(width=img.width(), height=img.height())
        frame.mainloop()

def getMapOrCfgFile(varName, entryName):
    varName = tkFileDialog.askopenfilename(filetypes=[("All files", "*"), ("Wesnoth Map Files", "*.map"), ("Wesnoth Game Files", "*.cfg")])
    entryName.insert(0, varName)

def quitButton():
    if tkMessageBox.askokcancel("Verify Quit", "Really quit?"):
        root.destroy()

def helpButton(helpMessage):
    tkMessageBox.showinfo(title="Help!", message=helpMessage)

#def createScenario():
#    scenName = nameEntry.get()
#    x = team('Bob the Great', 'Bowman', 'yes', 'human', '1', '100 200 300', '10', 'yes', 'no', 'The_Bears', 'Bowman, Spearman')
#    print x.SideVar

nameLabel = Label(root, width=13, text='Name:')
nameLabel.grid(column=0, row=0)

nameEntry = Entry(root, width=32)
nameEntry.grid(column=1, row=0)

nextScenarioLabel = Label(root, width=13, text='Next Scenario:')
nextScenarioLabel.grid(column=0, row=1)

nextScenarioEntry = Entry(root, width=32)
nextScenarioEntry.grid(column=1, row=1)

mapLabel = Label(root, width=13, text="Map File:")
mapLabel.grid(column=0, row=2)

mapEntry = Entry(root, width=32)
mapEntry.grid(column=1, row=2)

mapButton = Button(root, text="Browse", command=(lambda: getMapOrCfgFile(scenarioMap, mapEntry)))
mapButton.grid(column=2, row=2)

sideListLabel = Label(root, text="Sides:")
sideListLabel.grid(column=3, row=0, stick=W)

sideListBox = Listbox(root, width=40, height=20)
sideListBox.grid(column=3, row=1, columnspan=3, rowspan=21)

newSideButton = Button(root, text='New', command=createSide)
newSideButton.grid(column=3, row=22)

editSideButton = Button(root, text='Edit', command=None)
editSideButton.grid(column=4, row=22)

deleteSideButton = Button(root, text='Delete', command=None)
deleteSideButton.grid(column=5, row=22)

doneButton = Button(root, text="Done!", command=None)
doneButton.grid(column=0, row=22)

root.mainloop()

#print "What do you want the name of your scenario to be?"
#scenName = raw_input()
#print "Which number scenario is this? (this should be a number)"
#scenNumber = raw_input()
#print "How many sides will be in this "
#
#scenarioRootSplit = scenarioRoot.splitlines()
#
#scenarioRootSplit[2] += '_ "' + scenName + '"'
#scenarioRootSplit[3] += scenNumber + '_' + scenName.replace(' ', '_')
#for x in side.splitlines():
#    scenarioRootSplit.append(x)
#
#scenarioRootSplit.append("[/scenario]")
#
#scenarioRoot = "\n".join(scenarioRootSplit)
#
#print scenarioRoot
