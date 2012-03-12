from Tkinter import *
from ttk import *

def createSide():
    leadUnitType = None
    Canrecruit = StringVar()
    Controller = StringVar()
    Fog = StringVar()
    Shroud = StringVar()

    scenarioWindow = Toplevel()
    scenarioWindow.title("Create Team")
    #Leader Name Label & Entry
    leadNameLabel = Label(scenarioWindow, width=13, text="Leader's Name:")
    leadNameLabel.grid(column=0, row=0)
    
    leadNameEntry = Entry(scenarioWindow, width=32)
    leadNameEntry.grid(column=1, row=0, columnspan=2)
    #Leader Type Label, Entry, and Browse Button. The Browse Button will be for either finding a file, or looking through a list of units.
    leadTypeLabel = Label(scenarioWindow, width=13, text="Leader's Type:")
    leadTypeLabel.grid(column=0, row=1)
    
    leadTypeEntry = Entry(scenarioWindow, width=32)
    leadTypeEntry.grid(column=1, row=1, columnspan=2)
    
    leadTypeBrowse = Button(scenarioWindow, text='Browse', command=(lambda: getMapOrCfgFile(leadUnitType, leadTypeEntry)))
    leadTypeBrowse.grid(column=3, row=1)
    #Canrecruit Label & Radios
    canrecruitLabel = Label(scenarioWindow, text='Recruit?')
    canrecruitLabel.grid(column=0, row=2, sticky=W)
    
    canrecruitYes = Radiobutton(scenarioWindow, text='Yes', variable=Canrecruit, value='yes')
    canrecruitYes.grid(column=1, row=2, sticky=W)
  
    canrecruitNo = Radiobutton(scenarioWindow, text='No', variable=Canrecruit, value='no')
    canrecruitNo.grid(column=2, row=2, sticky=W)
    #Controller Label & Radios
    controllerLabel = Label(scenarioWindow, text='Controller:', width=13)
    controllerLabel.grid(column=0, row=3)
   
    controllerHuman = Radiobutton(scenarioWindow, text='Human', variable=Controller, value='human')
    controllerHuman.grid(column=1, row=3, sticky=W)
    
    controllerAI = Radiobutton(scenarioWindow, text='AI', variable=Controller, value='ai')
    controllerAI.grid(column=2, row=3, sticky=W)
    #Side Number Label & Entry
    sideNumLabel = Label(scenarioWindow, text='Side Number:', width=13)
    sideNumLabel.grid(column=0, row=4)
    
    sideNumEntry = Entry(scenarioWindow, width=32)
    sideNumEntry.grid(column=1, row=4, columnspan=2)
    #Gold Values
    goldLabel = Label(scenarioWindow, text='Gold:', width=13)
    goldLabel.grid(column=0, row=5)
    
    goldEntryEasy = Entry(scenarioWindow, width=10)
    goldEntryEasy.grid(column=1, row=5, sticky=W)
    
    goldEntryNormal = Entry(scenarioWindow, width=10)
    goldEntryNormal.grid(column=1, row=5, columnspan=2)

    goldEntryHard = Entry(scenarioWindow, width=10)
    goldEntryHard.grid(column=2, row=5, sticky=E)
    #Income Label & Entry
    incomeLabel = Label(scenarioWindow, text='Income', width=13)
    incomeLabel.grid(column=0, row=6)
    
    incomeEntry = Entry(scenarioWindow, width=32)
    incomeEntry.grid(column=1, row=6, columnspan=2)
    #Fog Label and Radios
    fogLabel = Label(scenarioWindow, text='Fog?', width=13)
    fogLabel.grid(column=0, row=7)

    fogYes = Radiobutton(scenarioWindow, text='Yes', variable=Fog, value='yes')
    fogYes.grid(column=1, row=7, sticky=W)
    
    fogNo = Radiobutton(scenarioWindow, text='No', variable=Fog, value='no')
    fogNo.grid(column=2, row=7, sticky=W)
    #Shroud Label and Radios
    shroudLabel = Label(scenarioWindow, text='Shroud?')
    shroudLabel.grid(column=0, row=8, sticky=W)
   
    shroudYes = Radiobutton(scenarioWindow, text='Yes', variable=Shroud, value='yes')
    shroudYes.grid(column=1, row=8, sticky=W)
    
    shroudNo = Radiobutton(scenarioWindow, text='No', variable=Shroud, value='no')
    shroudNo.grid(column=2, row=8, sticky=W)
    #Team name Label and Entry
    teamNameLabel = Label(scenarioWindow, text='Team Name:', width=13)
    teamNameLabel.grid(column=0, row=9)
    
    teamNameEntry = Entry(scenarioWindow, width=32)
    teamNameEntry.grid(column=1, row=9, columnspan=2)
    #
    recruitListLabel = Label(scenarioWindow, text="Sides:")
    recruitListLabel.grid(column=4, row=0, stick=W)

    recruitListBox = Listbox(scenarioWindow, width=40, height=20)
    recruitListBox.grid(column=4, row=1, columnspan=3, rowspan=21)

    newRecruitButton = Button(scenarioWindow, text='New', command=createSide)
    newRecruitButton.grid(column=4, row=22)

    deleteRecruitButton = Button(scenarioWindow, text='Delete', command=None)
    deleteRecruitButton.grid(column=5, row=22)

    doneButton = Button(scenarioWindow, text='Done!', command=createSide)
    doneButton.grid(column=0, row=22)
