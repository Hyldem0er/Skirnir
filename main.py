from src.ui import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
from src.utils.stylecss import GlobalStyleSheet
import argparse
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
    parser = argparse.ArgumentParser(description="Skirnir")
    
    # Add a --log argument to specify the log level (default is INFO)
    parser.add_argument("--log", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="CRITICAL", help="Set the log level")
    
    args = parser.parse_args()

    # Update the logger configuration based on the log level specified
    
    logger.remove()  # Remove the default logger configuration
    logger.add(sys.stdout, format="<green>{time}</green> <level>{message}</level>", level=args.log)
    logger.add("file.log", serialize=True, level="DEBUG")  # Log DEBUG and above to the log file

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