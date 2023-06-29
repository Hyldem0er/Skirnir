from src.ui import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
GlobalStyleSheet = ("""
            QWidget {
                background-color: #242933;
                color: white;
                font-size: 14px;
            }

            QLabel {
                color: white;
            }

            QGroupBox {
                border: 1px solid gray;
                border-radius: 5px;
                margin-top: 0.5em;
            }

            QGroupBox::title { 
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }

            QFormLayout::Label {
                color: white;
                font-weight: bold;
            }

            QTabWidget::pane {
                border: 1px solid #242933;
                top:-1px; 
                background: #0f0e18; 
            } 

            QTabBar::tab {
                background: #242933;
                padding: 10px;
            } 

            QTabBar::tab:selected { 
                border-top: 3px solid #7c2929;
                margin-bottom: -1px; 
            }

            QFormLayout::Line {
                color: white;
            }

            QCheckBox {
                color: #d5d1e5;
            }

            QCheckBox::indicator {
                border: 2px solid #bdbdca;
                background-color: transparent;
                width: 12px;
                height: 12px;
                border-radius: 7px;
            }

            QCheckBox::indicator:checked {
                border-color: red;
            }

            QSlider {
                color: white;
                height: 10px;
            }

            QSlider::groove:horizontal {
                background-color: white;
                height: 10px;
                border-radius: 5px;
            }

            QSlider::handle:horizontal {
                background-color: #e03d3d;
                width: 50px;
                height: 20px;
                border-radius: 3px;
            }

            QScrollBar:vertical {
                background-color: #16152b;
                width: 10px;
            }

            QScrollBar::handle:vertical {
                background-color: #7c2929;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #833030;
            }

            QScrollBar::handle:vertical:pressed {
                background-color: #833030;
            }

            QScrollBar::handle:vertical:selected {
                background-color: #833030;
            }

            QScrollBar:horizontal {
                background-color: #16152b;
                width: 10px;
            }

            QScrollBar::handle:horizontal {
                background-color: #7c2929;
            }

            QScrollBar::handle:horizontal:hover {
                background-color: #833030;
            }

            QScrollBar::handle:horizontal:pressed {
                background-color: #833030;
            }

            QScrollBar::handle:horizontal:selected {
                background-color: #833030;
            }

        """)


def main():
    """
    Entry point of the program.
    
    Initializes the QApplication, creates a Window object, shows the window,
    and starts the event loop. Upon exiting the event loop, the program will exit.
    """
    app = QApplication(sys.argv)
    # Apply the above Stylesheet to the application
    app.setStyleSheet(GlobalStyleSheet)
    window = MainWindow.MainWindow()
    window.show()
    sys.exit(app.exec())

# main method
if __name__ == '__main__':
    main()