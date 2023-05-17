from PyQt6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QMainWindow, QDial)
from PyQt6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('First App')
        button = QPushButton('This is a button.')

        self.create_horizontal_layout()
        self.setCentralWidget(self._horizontal_group_box)

        self.setFixedSize(QSize(200, 200))

    def create_horizontal_layout(self):
        self._horizontal_group_box = QGroupBox('Horizontal GroupBox')
        layout = QHBoxLayout()

        button = QPushButton(f'This is a button')
        layout.addWidget(button)
        layout.addWidget(QDial())

        self._horizontal_group_box.setLayout(layout)

        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

# window = QMainWindow()
# window.setWindowTitle('First App')
# window.show()

# CTRL + / to comment.
# window = QWidget()
# window.show()

app.exec()