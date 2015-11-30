import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

class Assignment4Widget(PyGlassWidget):

    global smileActAmt
    global schnauzActAmt
    global eyebrowsActAmt
    global eyebrowsIncAmt
    global incAmt

    smileActAmt = 0.000
    schnauzActAmt = 0.000
    eyebrowsActAmt = 0.000
    eyebrowsIncAmt = 0.007
    incAmt = 0.004

    def __init__(self, parent, **kwargs):
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.upBtn.clicked.connect(self.handleUpBtn)
        self.downBtn.clicked.connect(self.handleDownBtn)
        self.schnauzUpBtn.clicked.connect(self.handleSchnauzUpBtn)
        self.schnauzDownBtn.clicked.connect(self.handleSchnauzDownBtn)
        self.eyebrowUpBtn.clicked.connect(self.handleEyebrowsUpBtn)
        self.eyebrowDwnBtn.clicked.connect(self.handleEyebrowsDwnBtn)
        self.returnHomeBtn.clicked.connect(self.handleReturnHomeBtn)

    def handleUpBtn(self):
        global smileActAmt
        global incAmt
        topCapAmt = 0.016
        cmds.select('smileClusterHandle')
        smileActAmt += incAmt
        if smileActAmt <= topCapAmt:
            print smileActAmt
            cmds.move(0, smileActAmt, 0)
        else:
            smileActAmt = topCapAmt

    def handleDownBtn(self):
        global smileActAmt
        global incAmt
        btmCapAmt = -0.032
        cmds.select('smileClusterHandle')
        smileActAmt -= incAmt
        if smileActAmt >= btmCapAmt:
            print smileActAmt
            cmds.move(0, smileActAmt, 0)
        else:
            smileActAmt = btmCapAmt

    def handleSchnauzUpBtn(self):
        global schnauzActAmt
        global incAmt
        topCapAmt = 0.028
        cmds.select('schnauzClusterHandle')
        schnauzActAmt += incAmt
        if schnauzActAmt <= topCapAmt:
            print schnauzActAmt
            cmds.move(0, schnauzActAmt, 0)
        else:
            schnauzActAmt = topCapAmt

    def handleSchnauzDownBtn(self):
        global schnauzActAmt
        global incAmt
        btmCapAmt = 0.000
        cmds.select('schnauzClusterHandle')
        schnauzActAmt -= incAmt
        if schnauzActAmt >= btmCapAmt:
            print schnauzActAmt
            cmds.move(0, schnauzActAmt, 0)
        else:
            schnauzActAmt = btmCapAmt

    def handleEyebrowsUpBtn(self):
        global eyebrowsActAmt
        global eyebrowsIncAmt
        topCapAmt = 0.021
        cmds.select('eyebrowsClusterHandle')
        eyebrowsActAmt += eyebrowsIncAmt
        if eyebrowsActAmt <= topCapAmt:
            print eyebrowsActAmt
            cmds.move(0, eyebrowsActAmt, 0)
        else:
            eyebrowsActAmt = topCapAmt

    def handleEyebrowsDwnBtn(self):
        global eyebrowsActAmt
        global eyebrowsIncAmt
        btmCapAmt = -0.014
        cmds.select('eyebrowsClusterHandle')
        eyebrowsActAmt -= eyebrowsIncAmt
        if eyebrowsActAmt >= btmCapAmt:
            print eyebrowsActAmt
            cmds.move(0, eyebrowsActAmt, 0)
        else:
            eyebrowsActAmt = btmCapAmt

    def handleReturnHomeBtn(self):
        self.mainWindow.setActiveWidget('home')