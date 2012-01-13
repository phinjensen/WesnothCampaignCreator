import sys, os, tkFileDialog, tkMessageBox, glob, getpass, Tkinter, ImageTk
from Tkinter import *
from ttk import *

root = Tk()
root.title("_main.cfg Creator")
if sys.platform == 'linux2':
    Theme = Style()
    Theme.theme_use('clam')

# This is a function that gets the path to the icon, and puts it in the entry.
def getImageName(varName, entryName, issmallimage, canvasName, frame):
    varName = tkFileDialog.askopenfilename(filetypes=[("All files", "*.*"), ("PNG Images", "*.png")])
    entryName.insert(0, varName)
    if issmallimage:
        img = ImageTk.PhotoImage(file=varName)
        canvasName.create_image(2, 2, image=img, anchor=NW)
        canvasName.config(width=img.width(), height=img.height())
        frame.mainloop()

def quitButton():
    if tkMessageBox.askokcancel("Verify Quit", "Really quit?"):
        root.destroy()

def helpButton(helpMessage):
    tkMessageBox.showinfo(title="Help!", message=helpMessage)

def advancedOptionsWindow():
    optionsWindow = Toplevel()
    optionsWindow.title("Advanced Options")
    # All this is the labels and checks for the extra defines.              \
    extraDefinesChecksLabel = Label(optionsWindow, text="Extra Defines:")  #|
    extraDefinesChecksLabel.grid(column=0, row=0)                          #|
    extraDefines1 = Checkbutton(optionsWindow, text="Armegeddon Drake")    #|
    extraDefines2 = Checkbutton(optionsWindow, text='Ancient Lich')        #|
    extraDefines3 = Checkbutton(optionsWindow, text='Dwarvish Runecaster') #|
    extraDefines4 = Checkbutton(optionsWindow, text='Dwarvish Arcanister') #| All this. Oh, and get this: It doesn't actually do anything.
    extraDefines5 = Checkbutton(optionsWindow, text='Death Knight')        #|
    extraDefines1.grid(column=1, row=0)                                    #|
    extraDefines2.grid(column=2, row=0)                                    #|
    extraDefines3.grid(column=3, row=0)                                    #|
    extraDefines4.grid(column=4, row=0)                                    #|
    extraDefines5.grid(column=5, row=0)                                    #/
    #
    global EasyEntry, EasyIcon
    EasyLabel = Label(optionsWindow, text="Easy:")
    EasyLabel.grid(column=0, row=1)

    EasyCanvas = Tkinter.Canvas(optionsWindow, width=72, height=72)
    EasyCanvas.grid(column=1, row=1)

    EasyEntry = Entry(optionsWindow)
    EasyEntry.grid(column=2, row=1, columnspan=3, sticky=W+E)

    EasyIcon = None
    EasyBrowseButton = Button(optionsWindow, text="Browse", width=7, command=(lambda: getImageName(EasyIcon, EasyEntry, True, EasyCanvas, optionsWindow)))
    EasyBrowseButton.grid(column=5, row=1)
    #
    global MediumEntry, MediumIcon
    MediumLabel = Label(optionsWindow, text="Medium:")
    MediumLabel.grid(column=0, row=2)

    MediumCanvas = Tkinter.Canvas(optionsWindow, width=72, height=72)
    MediumCanvas.grid(column=1, row=2)

    MediumEntry = Entry(optionsWindow)
    MediumEntry.grid(column=2, row=2, columnspan=3, sticky=W+E)

    MediumIcon = None
    MediumBrowseButton = Button(optionsWindow, text="Browse", width=7, command=(lambda: getImageName(MediumIcon, MediumEntry, True, MediumCanvas, optionsWindow)))
    MediumBrowseButton.grid(column=5, row=2)
    #
    global HardEntry, HardIcon
    HardLabel = Label(optionsWindow, text="Hard:")
    HardLabel.grid(column=0, row=3)

    HardCanvas = Tkinter.Canvas(optionsWindow, width=72, height=72)
    HardCanvas.grid(column=1, row=3)

    HardEntry = Entry(optionsWindow)
    HardEntry.grid(column=2, row=3, columnspan=3, sticky=W+E)

    HardIcon = None
    HardBrowseButton = Button(optionsWindow, text="Browse", width=7, command=(lambda: getImageName(HardIcon, HardEntry, True, HardCanvas, optionsWindow)))
    HardBrowseButton.grid(column=5, row=3)
    #
    global NightmareEntry, NightmareIcon
    NightmareLabel = Label(optionsWindow, text="Nightmare:")
    NightmareLabel.grid(column=0, row=4)

    NightmareCanvas = Tkinter.Canvas(optionsWindow, width=72, height=72)
    NightmareCanvas.grid(column=1, row=4)

    NightmareEntry = Entry(optionsWindow)
    NightmareEntry.grid(column=2, row=4, columnspan=3, sticky=W+E)

    NightmareIcon = None
    NightmareBrowseButton = Button(optionsWindow, text="Browse", width=7, command=(lambda: getImageName(NightmareIcon, NightmareEntry, True, NightmareCanvas, optionsWindow)))
    NightmareBrowseButton.grid(column=5, row=4)


# The Final Function, which creates the _main.cfg file and creates the directorys.
def finalFunction():
    # Get the name...
    campName = nameEntry.get()
    # The First Scenario...
    campFirstScenario = firstScenarioEntry.get()
    # Description...
    campDescription = descriptionText.get(1.0, END)
    campDescription = campDescription.replace('''"''', """'""")
    # Icon...
    campIcon = iconEntry.get()
    # Cut off everything before 'core/images/', and then cut that off too.
    iconStringSliceNum = campIcon.find('core')
    campIcon = campIcon[iconStringSliceNum:]
    campIcon = campIcon.replace('core/images/', '')
    campImage = portraitEntry.get()
    # Same as above.
    imageStringSliceNum = campImage.find('core')
    campImage = campImage[imageStringSliceNum:]
    campImage = campImage.replace('core/images/', '')
    campId = campName.replace(' ', '_')
    # Create the abbreviation by using the campName variable...
    campAbbrev = campName.split()
    for i in range(len(campAbbrev)):
        campAbbrev[i] = campAbbrev[i][0:1]
    campAbbrev = ''.join(campAbbrev)
    # Create the difficulties.
    campDifficulties = ''
    checkButtonStrings = ['EASY,', 'MEDIUM,', 'HARD,', 'NIGHTMARE']
    if easyCheck.instate(['selected']):
        campDifficulties = checkButtonStrings[0]
    if normalCheck.instate(['selected']):
        campDifficulties = campDifficulties + checkButtonStrings[1]
    if hardCheck.instate(['selected']):
        campDifficulties = campDifficulties + checkButtonStrings[2]
    if nightmareCheck.instate(['selected']):
        campDifficulties = campDifficulties + checkButtonStrings[3]
    # Get difficulty description icons and names. I would put all this into a function, but it wouldn't work. Please give me any hints.
    EasyIcon = EasyEntry.get()
    EasyIconSliceNum = EasyIcon.find('core')
    EasyIcon = EasyIcon[EasyIconSliceNum:]
    EasyIcon = EasyIcon.replace('core/images/', '')
    #
    MediumIcon = MediumEntry.get()
    MediumIconSliceNum = MediumIcon.find('core')
    MediumIcon = MediumIcon[MediumIconSliceNum:]
    MediumIcon = MediumIcon.replace('core/images/', '')
    #
    HardIcon = HardEntry.get()
    HardIconSliceNum = HardIcon.find('core')
    HardIcon = HardIcon[HardIconSliceNum:]
    HardIcon = HardIcon.replace('core/images/', '')
    #
    NightmareIcon = NightmareEntry.get()
    NightmareIconSliceNum = NightmareIcon.find('core')
    NightmareIcon = NightmareIcon[NightmareIconSliceNum:]
    NightmareIcon = NightmareIcon.replace('core/images/', '')
    # Create the campaign defenition, just the Id, but uppercased...
    campDef = campId.upper()
    # Create the binary path...
    campBinary = 'data/add-ons/' + campId
    # The Template for the _main.cfg file...
    mainCfgTemplate = """
[campaign]
    id="%s"
    name= _ "%s"
    icon="%s"
    image=%s
    abbrev=%s
    first_scenario=%s
    difficulties=%s
    difficulty_descriptions=
    define=%s
    description="%s"
[/campaign]

#ifdef %s
    [binary_path]
        path=%s
    [/binary_path]
    {~add-ons/%s/utils}
    [+units]
        {~add-ons/%s/units}
    [/units]
    {~add-ons/%s/scenarios}
#endif
""" %(campId, campName, campIcon, campImage, campAbbrev, campFirstScenario, campDifficulties, campDef, campDescription, campDef, campBinary, campId, campId, campId)
    mainCfgList = mainCfgTemplate.split('\n') 

    if "EASY" in mainCfgTemplate:
        mainCfgList[9] += ' {MENU_IMG_TXT2 "' + EasyIcon + '" (_ 'Trainee') (_ "(Easy)")} + ";" +' 

    if "MEDIUM" in mainCfgTemplate:
        mainCfgList[9] += ' {MENU_IMG_TXT2 "' + MediumIcon + '" (_ "Soldier") (_ "(Medium)")} + ";" +'

    if "HARD" in mainCfgTemplate:
        mainCfgList[9] += ' {MENU_IMG_TXT2 "' + HardIcon + '" (_ "General") (_ "(Hard)")} + ";" +'

    if "NIGHTMARE" in mainCfgTemplate:
        mainCfgList[9] += ' {MENU_IMG_TXT2 "' + NightmareIcon + '" (_ "Master") (_ "(Nightmare)")}' 

    if mainCfgList[9].endswith('+'):
        mainCfgList[9] = mainCfgList[9][0:-8]

    mainCfgTemplate = '\n'.join(mainCfgList)
    
    print mainCfgTemplate

    # Find the Userdata directory using the command wesnoth --config-path. The create the paths.

    if sys.platform == "linux2" or sys.platform == "darwin":
        userDataPath = os.popen("wesnoth --config-path").read()
        if not userDataPath:
            tkMessageBox.askokcancel("Userdata not found!", "Your userdata directory was not found! Please locate it.")
            userDataPath = tkFileDialog.askdirectory()
	userDataPath = userDataPath.strip() + '/'
    elif sys.platform == "win32":
        userName = getpass.getuser()
        userDataPath = glob.glob('C:\\Users\\' + userName + "\\Documents\\My Games\\Wesnoth[0-9]*")
        userDataPath.sort(key=lambda path:[int(x) for x in re.findall("[0-9]+",path)], reverse=True)
	if len(userDataPath) > 1:
            userDataPath = userDataPath[0]
        else:
            userDataPath = str(userDataPath[0])
    else:
        print "Error!"

    if sys.platform == "linux2":
        campPath = userDataPath + campBinary + '/'
    elif sys.platform == "win32":
        campPath = userDataPath + '\\data\\add-ons\\' + campId + '\\'
	if not os.path.exists(userDataPath):
            tkMessageBox.askokcancel("Userdata not found!", "Your userdata directory was not found! Please locate it.")
            userDataPath = tkFileDialog.askdirectory()
            userDataPath = userDataPath.replace('/', '\\')
            userDataPath = str(userDataPath)
            campPath = userDataPath + '\\data\\add-ons\\' + campId + '\\'
    else:
        campPath = userDataPath + '\\data\\add-ons\\' + campId + '\\'

    # Create Folders.
    os.mkdir(campPath)
    os.mkdir(campPath + 'scenarios/')
    os.mkdir(campPath + 'maps/')
    os.mkdir(campPath + 'utils/')
    os.mkdir(campPath + 'units/')
    os.mkdir(campPath + 'images/')
    # Finally, Write to the file.
    mainCfgHandle = open(campPath + '_main.cfg', 'w')
    mainCfgHandle.write(mainCfgTemplate)
    root.quit()
    tkMessageBox.showinfo(title="Congratulations!", message="You now have a _main.cfg file for your campaign! This file is just the file that puts the campaign in the list. To create scenarios, I suggest you visit http://www.wiki.wesnoth.org/create/ where there are tutorials on creating the scenario files. You can also find help on the Forums, at forums.wesnoth.org. Thanks!")

# Create and pack the frames
openingRow = Frame(root)
nameRow = Frame(root)
firstScenarioRow = Frame(root)
descRow = Frame(root)
diffRow = Frame(root)
iconRow = Frame(root)
portraitRow = Frame(root)

openingRow.pack(side=TOP, fill=X)
nameRow.pack(side=TOP, fill=X)
firstScenarioRow.pack(side=TOP, fill=X)
descRow.pack(side=TOP, fill=BOTH, expand=YES)
diffRow.pack(side=TOP, fill=X)
iconRow.pack(side=TOP, fill=BOTH)
portraitRow.pack(side=TOP, fill=BOTH)

# Welcome Label
openingLabel = Message(openingRow, width=90, text="So, you want to make a campaign? Great! This script is designed to make it easy for people who aren't aquianted with WML (Wesnoth Markup Language). Just fill in the blanks, and the rest will be done from there! I you need help, just click one of the buttons marked with a question mark")
openingLabel.pack(side=TOP, fill=X)
openingLabel.bind("<Configure>", lambda e: openingLabel.configure(width=e.width-10))
# Label and Entry for the name row
nameLabel = Label(nameRow, width=15, text="Name:")
nameLabel.pack(side=LEFT)
          
nameEntry = Entry(nameRow, width=50)
nameEntry.pack(side=LEFT, fill=X, expand=YES)

nameHelpButton = Button(nameRow, text="?", command=(lambda: helpButton("This is where the name of the Campaign you want to create goes.")), width=1)
nameHelpButton.pack(side=RIGHT)

# Label and Entry for the first scenario row...
firstScenarioLabel = Label(firstScenarioRow, width=15, text='First Scenario ID:')
firstScenarioLabel.pack(side=LEFT)

firstScenarioEntry = Entry(firstScenarioRow, width=50)
firstScenarioEntry.pack(side=LEFT, fill=X, expand=YES)

firstScenarioHelpButton = Button(firstScenarioRow, width=1, text="?", command=(lambda: helpButton("This is where the ID of the first scenario of your campaign is. The ID would usually be the name of the first scenario, with underscores instead of spaces, and the scenario number at the beginning.")))
firstScenarioHelpButton.pack(side=RIGHT)

# Label, Text Widget, and Scrollbar for the discription...
descriptionLabel = Label(descRow, width=15, text='Description:')
descriptionLabel.pack(side=LEFT, expand=NO)

sbar = Scrollbar(descRow)
descriptionText = Text(descRow, relief=SUNKEN, width=50, height=8)
sbar.config(command=descriptionText.yview)
descriptionText.config(yscrollcommand=sbar.set)
descriptionText.pack(side=LEFT, fill=BOTH, expand=YES)
sbar.pack(side=LEFT, fill=Y)

diffLabel=Label(diffRow,width=15,text='Difficult Levels:')
diffLabel.pack(side=LEFT)

easyCheck=Checkbutton(diffRow,text='Easy', onvalue=1)
easyCheck.pack(side=LEFT)

normalCheck=Checkbutton(diffRow,text='Normal', onvalue=1)
normalCheck.pack(side=LEFT)

hardCheck=Checkbutton(diffRow,text='Hard', onvalue=1)
hardCheck.pack(side=LEFT)

nightmareCheck=Checkbutton(diffRow,text='Nightmare', onvalue=1)
nightmareCheck.pack(side=LEFT)

checkButtonsHelpButton = Button(diffRow, text="?", width=1, command=(lambda: helpButton("This is where you choose the number of difficulties. For Icons and names of difficulties, open the advanced options window.")))
checkButtonsHelpButton.pack(side=RIGHT)

descriptionHelpButton = Button(descRow, width=1, text="?", command=(lambda: helpButton("This is where the description for the campaign should go.")))
descriptionHelpButton.pack(side=RIGHT)

# Label, Entry, and Browse button for the Icon
iconLabel = Label(iconRow, width=15, text='Campaign Icon:')
iconLabel.pack(side=LEFT)

iconCanvas = Canvas(iconRow)
iconCanvas.pack(side=LEFT)
iconCanvas.config(width=72, height=72)

iconEntry = Entry(iconRow, width=50)
iconEntry.pack(side=LEFT, fill=X, expand=YES)

campIcon = ''
iconButton = Button(iconRow, width=7, text="Browse", command=(lambda: getImageName(campIcon, iconEntry, True, iconCanvas, iconRow)))
iconButton.pack(side=LEFT)

iconHelpButton = Button(iconRow, width=1, text="?", command=(lambda: helpButton("This is the small icon that would go next to the name of the campaign. This should be an image from the core game.")))
iconHelpButton.pack(side=RIGHT)

# Label, Entry, and Browse button for the Portrait
portraitLabel = Label(portraitRow, width=15, text='Portrait:')
portraitLabel.pack(side=LEFT)

portraitEntry = Entry(portraitRow, width=50)
portraitEntry.pack(side=LEFT, fill=X, expand=YES)

campImage = ''
portraitButton = Button(portraitRow, width=7, text="Browse", command=(lambda: getImageName(campImage, portraitEntry, None, None, None)))
portraitButton.pack(side=LEFT)

portraitHelpButton = Button(portraitRow, width=1, text="?", command=(lambda: helpButton("This is the portrait that goes underneath the description.")))
portraitHelpButton.pack(side=RIGHT)

advancedOptionsButton = Button(root, text="Advanced Options", command=(lambda: advancedOptionsWindow()))
advancedOptionsButton.pack()

Button(root, text="Done!", command=finalFunction).pack(side=LEFT)
Button(root, text="Quit", command=quitButton).pack(side=RIGHT)

root.mainloop()
