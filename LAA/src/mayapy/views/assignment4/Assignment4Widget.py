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
        self.smileSlider.valueChanged.connect(self.handleSmileSlider)
        self.schnauzSlider.valueChanged.connect(self.handleSchnauzSlider)
        self.eyebrowSlider.valueChanged.connect(self.handleEyebrowSlider)
        self.widenSlider.valueChanged.connect(self.handleWidenSlider)
        self.lengthSlider.valueChanged.connect(self.handleLengthSlider)
        self.returnHomeBtn.clicked.connect(self.handleReturnHomeBtn)

    def handleWidenSlider(self):
        value = self.widenSlider.value()
        cmds.setAttr('headWideBlendShape.amandaHeadWide', value)

    def handleLengthSlider(self):
        value = self.lengthSlider.value()
        cmds.setAttr('headWideBlendShape.amandaHeadTall', value)

    def handleSmileSlider(self):
        topCapAmt = 0.016
        btmCapAmt = -0.032
        value = self.smileSlider.value()
        smileValue = float(value) * float(topCapAmt/10.0)
        if value < 0:
            lowSmileValue = float(value) * float(btmCapAmt/10.0)
            cmds.setAttr('smileClusterHandle.translateY', -lowSmileValue)
        else:
            cmds.setAttr('smileClusterHandle.translateY', smileValue)

    def handleSchnauzSlider(self):
        topCapAmt = 0.028
        btmCapAmt = 0.000
        value = self.schnauzSlider.value()
        schnauzValue = float(value) * float(topCapAmt/10.0)
        if value < 0:
            lowSchnauzValue = float(value) * float(btmCapAmt/10.0)
            cmds.setAttr('schnauzClusterHandle.translateY', -lowSchnauzValue)
        else:
            cmds.setAttr('schnauzClusterHandle.translateY', schnauzValue)

    def handleEyebrowSlider(self):
        topCapAmt = 0.021
        btmCapAmt = -0.014
        value = self.eyebrowSlider.value()
        eyebrowValue = float(value) * float(topCapAmt/10.0)
        if value < 0:
            lowEyebrowValue = float(value) * float(btmCapAmt/10.0)
            cmds.setAttr('eyebrowsClusterHandle.translateY', -lowEyebrowValue)
        else:
            cmds.setAttr('eyebrowsClusterHandle.translateY', eyebrowValue)

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