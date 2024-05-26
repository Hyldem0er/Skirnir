GlobalStyleSheet = ("""

            QDialog {
                background-color: #242933;
            }  
            
            QWidget {
                color: white;
                font-size: 14px;
            }
            
            QLineEdit {
                background-color: #242933;
            }
                    
            QPushButton {
                background-color: #242933;
            }

            QLabel {
                color: white;
                background-color: #242933;

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
                    
            QFormLayout::Line {
                color: white;
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
                    
            QDateEdit {
                color: black
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
                    
            QSlider::groove:horizontal {
                background: #1e222a;
                border-radius: 10px;
            }

            QSlider::handle {
                background:  white;
                width: 12px;
                height: 19.5px;
                border-radius: 5px;
                border: 0.5px solid #151517;
            }

            QSlider::sub-page:horizontal {
                background: #151517;
            }

            QRangeSlider {
                qproperty-barColor:#9797a9;
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

range_style_sheet = ("""
    QSlider::groove:horizontal {
        background: #1e222a;
        border-radius: 10px;
    }

    QSlider::handle {
        background: white;
        width: 12px;
        height: 19.5px;
        border-radius: 5px;
        border: 0.5px solid #151517;
    }

    QSlider::sub-page:horizontal {
        background: #151517;
    }

    QRangeSlider {
        qproperty-barColor: #9797a9;
    }
    """)


result_style_sheet = ("""
  QWidget {
                background-color: #242933;
                color: white;
                font-size: 14px;
            }
""")