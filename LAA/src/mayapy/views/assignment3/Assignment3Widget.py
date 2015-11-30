import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

class Assignment3Widget(PyGlassWidget):

    def __init__(self, parent, **kwargs):
        super(Assignment3Widget, self).__init__(parent, **kwargs)
        self.scriptBtn.clicked.connect(self.handleScriptBtn)
        self.animateLegsBtn.clicked.connect(self.handleLegsBtn)
        self.animateBallBtn.clicked.connect(self.handleBallBtn)
        self.homeBtn.clicked.connect(self.handleReturnHome)

    def handleScriptBtn(self):
        cmds.select('arm_R')
        cmds.currentTime(1)
        cmds.setKeyframe('arm_R', at='rotateX')

        cmds.currentTime(20)
        cmds.rotate(-142.85, 0, 0)
        cmds.setKeyframe('arm_R', at='rotateX')

        cmds.currentTime(32)
        cmds.rotate(-142.85, 0, 0)
        cmds.setKeyframe('arm_R', at='rotateX')

        cmds.currentTime(48)
        cmds.rotate(0, 0, 0)
        cmds.setKeyframe('arm_R', at='rotateX')

    def handleLegsBtn(self):
        cmds.select('leg_R')
        cmds.currentTime(48)
        cmds.setKeyframe('leg_R', at='rotateX')

        cmds.currentTime(64)
        cmds.rotate(70.63, 0, 0)
        cmds.setKeyframe('leg_R', at='rotateX')

        cmds.currentTime(80)
        cmds.rotate(-64.254, 0, 0)
        cmds.setKeyframe('leg_R', at='rotateX')

        cmds.currentTime(96)
        cmds.rotate(0, 0, 0)
        cmds.setKeyframe('leg_R', at='rotateX')

        cmds.currentTime(104)
        cmds.rotate(12.526, 0, 0)
        cmds.setKeyframe('leg_R', at='rotateX')

        cmds.currentTime(107)
        cmds.rotate(0, 0, 0)
        cmds.setKeyframe('leg_R', at='rotateX')

    def handleBallBtn(self):
        cmds.select('ball')
        cmds.currentTime(74)
        cmds.setKeyframe('ball')

        cmds.currentTime(112)
        cmds.move(-0.757, 6.434, 15.831)
        cmds.rotate(9.208, 17.386, -368.887)
        cmds.setKeyframe('ball')

        cmds.currentTime(144)
        cmds.move(-0.772, 0.637, 22.462)
        cmds.rotate(9.208, 17.386, -368.887)
        cmds.setKeyframe('ball')

    def handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')