from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

scriptDir = os.path.dirname(os.path.realpath(__file__))
gifFile = (scriptDir + os.path.sep + 'loading.gif')

class Loading(QWidget):
    """
    A custom widget for displaying a loading animation.

    Attributes:
        label (QLabel): Label to display the animation.
        movie (QMovie): Movie object to handle the animation.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Popup Window")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(240, 240)

        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)

        self.movie = QMovie(gifFile)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.setLayout(layout)
