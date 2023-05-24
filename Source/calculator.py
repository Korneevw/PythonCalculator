from PyQt6.QtWidgets import (QApplication, QMainWindow)
from calculator_ui import Ui_TheNamelessCalculator

from math import sqrt

import sys

class MainWindow(QMainWindow):

    DECIMAL_PRECISION = 8

    storedNumber = 0
    lastWrittenNumber = 0
    writtenNumber = ''

    operation = ''
    
    result = 0

    repeatLastOperation = False

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_TheNamelessCalculator()
        self.ui.setupUi(self)

        self.ui.oneButton.clicked.connect(lambda: self.write_number(1))
        self.ui.twoButton.clicked.connect(lambda: self.write_number(2))
        self.ui.threeButton.clicked.connect(lambda: self.write_number(3))
        self.ui.fourButton.clicked.connect(lambda: self.write_number(4))
        self.ui.fiveButton.clicked.connect(lambda: self.write_number(5))
        self.ui.sixButton.clicked.connect(lambda: self.write_number(6))
        self.ui.sevenButton.clicked.connect(lambda: self.write_number(7))
        self.ui.eightButton.clicked.connect(lambda: self.write_number(8))
        self.ui.nineButton.clicked.connect(lambda: self.write_number(9))
        self.ui.zeroButton.clicked.connect(lambda: self.write_number(0))
        self.ui.dotButton.clicked.connect(lambda: self.write_number('.'))

        self.ui.sqrtButton.clicked.connect(self.square_root)

        self.ui.plusButton.clicked.connect(lambda: self.set_operation('+'))
        self.ui.minusButton.clicked.connect(lambda: self.set_operation('-'))
        self.ui.multiplyButton.clicked.connect(lambda: self.set_operation('*'))
        self.ui.divideButton.clicked.connect(lambda: self.set_operation(':'))
        self.ui.remainderButton.clicked.connect(lambda: self.set_operation('%'))
        self.ui.powerButton.clicked.connect(lambda: self.set_operation('^'))

        self.ui.equalsButton.clicked.connect(self.calculate)

        self.ui.backspaceButton.clicked.connect(self.backspace)
        self.ui.clearButton.clicked.connect(self.clear)
        
        self.setWindowTitle('The Nameless Calculator')

    def write_number(self, numberOrDot):
        if numberOrDot == '.':
            if '.' in self.writtenNumber or self.writtenNumber == '':
                return
        elif numberOrDot == 0:
            if self.writtenNumber == '':
                return
        self.writtenNumber += str(numberOrDot)
        self.lastWrittenNumber = self.writtenNumber
        self.ui.fieldLineEdit.setText(self.writtenNumber)

    def backspace(self):
        if self.writtenNumber == '':
            return
        self.writtenNumber = self.writtenNumber[:-1]
        self.lastWrittenNumber = self.writtenNumber
        self.ui.fieldLineEdit.setText(self.writtenNumber)

    def clear(self):
        self.writtenNumber = ''
        self.storedNumber = 0
        self.lastWrittenNumber = 0
        self.result = 0
        self.operation = ''
        self.ui.fieldLineEdit.setText('')

    def square_root(self):
        if self.result != 0 and self.writtenNumber == '' and self.storedNumber == 0:
            self.result = sqrt(self.result)
            self.ui.fieldLineEdit.setText(str(self.result))
            return
        elif self.writtenNumber == '':
            self.ui.fieldLineEdit.setText('Enter a number at first')
            return
        self.writtenNumber = str(round(sqrt(float(self.writtenNumber)), self.DECIMAL_PRECISION))
        self.ui.fieldLineEdit.setText(self.writtenNumber)

    def set_operation(self, operation):
        if self.writtenNumber != '' and self.storedNumber != 0:
            self.calculate()
        elif self.writtenNumber == '' and self.result == 0:
            self.ui.fieldLineEdit.setText('Enter a number at first')
            return
        self.operation = operation
        if self.writtenNumber != '':
            self.storedNumber = round(float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.result != 0:
            self.storedNumber = self.result
        self.writtenNumber = ''
        self.ui.fieldLineEdit.setText(operation)

    def calculate(self):
        if self.storedNumber == 0 and self.writtenNumber == '':
            self.storedNumber = self.result
            self.writtenNumber = self.lastWrittenNumber
        if self.writtenNumber == '':
            self.ui.fieldLineEdit.setText('Enter the second number')
            return
        if self.operation == '+':
            self.result = round(self.storedNumber + float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.operation == '-':
            self.result = round(self.storedNumber - float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.operation == '*':
            self.result = round(self.storedNumber * float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.operation == ':':
            self.result = round(self.storedNumber / float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.operation == '%':
            self.result = round(self.storedNumber % float(self.writtenNumber), self.DECIMAL_PRECISION)
        elif self.operation == '^':
            self.result = round(self.storedNumber ** float(self.writtenNumber), self.DECIMAL_PRECISION)
        self.storedNumber = 0
        self.writtenNumber = ''
        self.ui.fieldLineEdit.setText(str(self.result))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())