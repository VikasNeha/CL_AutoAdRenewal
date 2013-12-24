import gui
import os
import sys
import CL_AutoAdRenewal
import config
from Utilities.myLogger import logger

# --- here goes your event handlers ---


def openInputXLS(evt):
    if os.path.isfile(mywin['txtInputXLS'].value):
        #startcommand = 'start excel "' + mywin['txtInputXLS'].value + '"'
        startcommand = '"' + mywin['txtInputXLS'].value + '"'
        os.popen(startcommand)
    else:
        gui.alert("Please select a valid Input XLS first.")


def openOutputXLS(evt):
    if os.path.isfile(mywin['txtOutputXLS'].value):
        #startcommand = 'start excel "' + mywin['txtOutputXLS'].value + '"'
        startcommand = '"' + mywin['txtOutputXLS'].value + '"'
        os.popen(startcommand)
    else:
        gui.alert("Output XLS file does not exist.")


def setOutputPaths():
    resourcesDir = os.path.dirname(mywin['txtInputXLS'].value)
    mywin['txtOutputXLS'].value = resourcesDir + "\\Output.xls"
    mywin['txtOutputImages'].value = resourcesDir + "\\Images\\"


def setDefaultInputXLS(evt):
    fileName = "Resources\\Input.xls"
    excelfile = config.get_main_dir() + "\\" + fileName
    mywin['txtInputXLS'].value = excelfile
    setOutputPaths()


def browseInputXLS(evt):
    from gui import dialog

    inputFile = dialog.open_file(title="Browse Input XLS",
                                 directory=config.get_main_dir() + "/Resources/",
                                 wildcard='Excel files (*.xls)|*.xls', )
    if inputFile is not None:
        mywin['txtInputXLS'].value = inputFile
        setOutputPaths()


def load(evt):
    setDefaultInputXLS(evt)
    mywin['statusbar'].text = 'CraigsList Auto Ad Renewal Software. Powered by K Team !!!'


def doAutoRenewal(evt):
    if os.path.isfile(mywin['txtInputXLS'].value):
        if not os.path.isdir(mywin['txtOutputImages'].value):
            os.makedirs(mywin['txtOutputImages'].value)
        config.inputXLSPath = mywin['txtInputXLS'].value
        config.outputXLSPath = mywin['txtOutputXLS'].value
        config.outputImagesPath = mywin['txtOutputImages'].value
        mywin['btnOpenOutput'].enabled = False
        mywin.minimized = True
        mywin.enabled = False
        # noinspection PyBroadException
        try:
            retValue = CL_AutoAdRenewal.main()
            mywin.enabled = True
            mywin.minimized = False
            mywin['btnOpenOutput'].enabled = True

            if retValue == 1:
                mbResponse = gui.confirm(
                    message="Thanks for using CL_AutoAdRenewal by K Team \nDo you want to open output file?",
                    title="All Renewals Complete !",
                )
                if mbResponse:
                    openOutputXLS(evt)
        except:
            logger.exception(sys.exc_info())
        finally:
            mywin.enabled = True
            mywin.minimized = False
    else:
        gui.alert("Please select a valid Input XLS first.")

# --- gui2py designer generated code starts ---

#======== MAIN WINDOW ========#
gui.Window(name=u'CL_AutoAdRenewal',
           title=u'CraigsList Auto Ad Renewal Software',
           maximize_box=False, resizable=False, height='400px', left='173',
           top='58', width='550px', bgcolor=u'#E0E0E0', fgcolor=u'#000000',
           image=config.get_main_dir()+'/Resources/tile.bmp', tiled=True, )

#======== HEADER LABELS ========#
gui.Label(id=281, name='label_211_281', height='17', left='50', top='40',
          width='254', transparent=True,
          font={'size': 9, 'family': 'sans serif', 'face': u'Arial'},
          parent=u'CL_AutoAdRenewal',
          text=u'Welcome to CraigsList Auto Ad Renewal Software', )
gui.Label(name='label_211', height='46', left='50', top='69', width='0',
          font={'size': 9, 'family': 'sans serif', 'face': u'Arial'},
          parent=u'CL_AutoAdRenewal', transparent=True,
          text=u'Please provide correct input details and format to ensure proper Auto Ad Renewals.', )

#======== INPUT XLS SECTION ========#

#----- Input XLS Label -----#
gui.Label(id=429, name='label_302_348_429', height='17', left='50', top='110',
          width='131', parent=u'CL_AutoAdRenewal', transparent=True,
          text=u'Browse for Input XLS file:', )
#----- Browse Button -----#
gui.Button(label=u'Browse...', name=u'btnBrowseInput', left='194', top='105',
           fgcolor=u'#000000', parent=u'CL_AutoAdRenewal', transparent=True, )
#----- Select Default Input Button -----#
gui.Button(id=205, label=u'Select Default', name=u'btnInputDefault',
           left='295', top='105', width='107', fgcolor=u'#000000',
           parent=u'CL_AutoAdRenewal', transparent=True, )
#----- Input XLS textbox -----#
gui.TextBox(id=573, name=u'txtInputXLS', height='23', left='50',
            sizer_align='center', top='135', width='428', bgcolor=u'#FFFFFF',
            editable=False, fgcolor=u'#000000', parent=u'CL_AutoAdRenewal', transparent=True, )
#----- Open Input XLS Button -----#
gui.Button(label=u'Open Input XLS', name=u'btnOpenInput', height='33',
           left='371', top='163', width='108',
           fgcolor=u'#000000', parent=u'CL_AutoAdRenewal', transparent=True, )

#======== OUTPUT XLS SECTION ========#

#----- Output XLS Label -----#
gui.Label(id=348, name='label_302_348', height='17', left='50', top='180',
          width='131', parent=u'CL_AutoAdRenewal',
          text=u'Output XLS fil'
               u'e will be available at:', transparent=True, )
#----- Output XLS textbox -----#
gui.TextBox(id=469, name=u'txtOutputXLS', height='23', left='50',
            sizer_align='center', top='205', width='428', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'CL_AutoAdRenewal', transparent=True,
            value=u'Please select Input XLS first...', )
#----- Open Output XLS Button -----#
gui.Button(label=u'Open Output XLS', name=u'btnOpenOutput', height='33',
           left='371', top='233', width='108', enabled=False,
           fgcolor=u'#000000', parent=u'CL_AutoAdRenewal', transparent=True, )

#======== OUTPUT IMAGES SECTION ========#

#----- Output Images Label -----#
gui.Label(id=349, name='label_302_348', height='17', left='50', top='250',
          width='131', parent=u'CL_AutoAdRenewal', transparent=True,
          text=u'Output Images will be available at:', )
#----- Output Images textbox -----#
gui.TextBox(id=470, name=u'txtOutputImages', height='23', left='50',
            sizer_align='center', top='275', width='428', bgcolor=u'#FFFFFF',
            editable=False, enabled=False, fgcolor=u'#000000',
            parent=u'CL_AutoAdRenewal', transparent=True,
            value=u'Please select Input XLS first...', )

#======== DO AUTO RENEWAL BUTTON ========#
gui.Button(label=u'Do Auto Ad Renewal', name=u'btnDoRenewal', height='39',
           left='185', top='327', width='292', fgcolor=u'#000000',
           font={'size': 11, 'family': 'sans serif', 'face': u'Tahoma'},
           parent=u'CL_AutoAdRenewal', transparent=True, )

gui.StatusBar(name='statusbar', parent=u'CL_AutoAdRenewal', )

gui.Image(name='image_148', height='40', left='440', top='5', width='100',
          fgcolor=u'#000000',
          filename=config.get_main_dir()+'/Resources/python-powered.bmp',
          parent=u'CL_AutoAdRenewal', stretch=False, transparent=False, border='static')

# --- gui2py designer generated code ends ---

# get a reference to the Top Level Window:
mywin = gui.get("CL_AutoAdRenewal")

# assign your event handlers:
mywin.onload = load
mywin['btnOpenInput'].onclick = openInputXLS
mywin['btnInputDefault'].onclick = setDefaultInputXLS
mywin['btnBrowseInput'].onclick = browseInputXLS
mywin['btnDoRenewal'].onclick = doAutoRenewal
mywin['btnOpenOutput'].onclick = openOutputXLS

if __name__ == "__main__":
    # myLogger.setupLogging()
    mywin.show()
    gui.main_loop()