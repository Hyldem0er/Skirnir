import sys, os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton
scriptDir = os.path.dirname(os.path.realpath(__file__))
gifFile = (scriptDir + os.path.sep + 'loading.gif')


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Popup Dialog")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)

        self.movie = QMovie(gifFile)
        self.label.setMovie(self.movie)
        self.movie.start()

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = CustomDialog()
    dialog.show()

    sys.exit(app.exec_())