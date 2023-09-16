from src.ui import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
from src.utils.stylecss import GlobalStyleSheet

from loguru import logger


# For scripts
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "<green>{time}</green> <level>{message}</level>"},
        {"sink": "file.log", "serialize": True},
    ],
}
logger.configure(**config)

def main():
    """
    Entry point of the program.
    
    Initializes the QApplication, creates a Window object, shows the window,
    and starts the event loop. Upon exiting the event loop, the program will exit.
    """
    logger.info("Enter the program")
    app = QApplication(sys.argv)
    # Apply the above Stylesheet to the application
    app.setStyleSheet(GlobalStyleSheet)
    window = MainWindow.MainWindow()
    window.show()
    sys.exit(app.exec())


# main method
if __name__ == '__main__':
    main()