from PyQt6.QtWidgets import (QApplication, QMainWindow) # Позволяем использовать классы приложения и окна из библиотеки PyQt в этом файле.
from calculator_ui import Ui_TheNamelessCalculator # Позволяем использовать UI калькулятора в этом файле.

from math import sqrt # Позволяем использовать функцию квадратного корня из библиотеки math в этом файле.

import sys

class MainWindow(QMainWindow):

    # Точность округления дробных чисел.
    DECIMAL_PRECISION = 8

    
    # Введённое число, сохранённое для вычислений.
    storedNumber = 0
    # Последнее введённое число, если требуется повторять операцию после получения результата.
    lastWrittenNumber = 0
    # Число, вводимое пользователем. Строка.
    writtenNumber = ''

    # Текущая операция
    operation = ''
    
    # Результат
    result = 0

    def __init__(self):
        # Вызываем конструктор (метод, который вызывается при создании экземпляра класса) вышестоящего по иерархии наследования класса (super)
        super().__init__()
        
        # Инициализируем пользовательский интерфейс.
        # self.ui - переменная пользовательского интерфейса в этом классе.
        self.ui = Ui_TheNamelessCalculator()
        self.ui.setupUi(self)

        # Устанавливаем обработчики при нажатии на кнопки, отвечающие за ввод числа.
        # Так как мы не можем передать в функцию "connect" кнопки функцию с параметрами, то мы пользуемся лямбда-выражением,
        # которое само создаст функцию (которую нельзя переиспользовать) без параметров, в которой мы вызываем другую функцию "self.write_number"
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

        # Устанавливаем отдельный обработчик для 
        self.ui.sqrtButton.clicked.connect(self.square_root)

        # Устанавливаем обработчики при нажатии на кнопки, отвечающие за выбор операции.
        self.ui.plusButton.clicked.connect(lambda: self.set_operation('+'))
        self.ui.minusButton.clicked.connect(lambda: self.set_operation('-'))
        self.ui.multiplyButton.clicked.connect(lambda: self.set_operation('*'))
        self.ui.divideButton.clicked.connect(lambda: self.set_operation(':'))
        self.ui.remainderButton.clicked.connect(lambda: self.set_operation('%'))
        self.ui.powerButton.clicked.connect(lambda: self.set_operation('^'))

        # Устанавливаем обработчик при нажатии на кнопку "=".
        self.ui.equalsButton.clicked.connect(self.calculate)

        # Устанавливаем обработчики при нажатии на кнопки "backspace" и "C" 
        self.ui.backspaceButton.clicked.connect(self.backspace)
        self.ui.clearButton.clicked.connect(self.clear)
        
        # Устанавливаем название окна приложения.
        self.setWindowTitle('The Nameless Calculator')

    # Функция, отвечающая за ввод числа.
    # numberOrDot - число или точка, которые нужно добавить к введённому числу.
    def write_number(self, numberOrDot):
        # Точку нельзя поставить, если в числе уже есть точка, либо если число пустое (точка не может стоять первой)
        if numberOrDot == '.': # Если мы хотим ввести точку:
            if '.' in self.writtenNumber or self.writtenNumber == '': # Если точка уже есть в числе ИЛИ переменная числа - пустая,
                return # то мы прекращаем выполнение функции.
            
        # Сюда мы попадаем, если число или точку можно поставить. В противном случае осуществляется выход из функции посредством return, и ничего не происходит.
        self.writtenNumber += str(numberOrDot) # Прибавляем к введённому числу (строке) данный символ (число или точку).
        self.lastWrittenNumber = self.writtenNumber # Сохраняем полученное число. Зачем - дальше по коду станет ясно.
        self.ui.fieldLineEdit.setText(self.writtenNumber) # "Показываем" полученное число пользователю, установив текст в поле ввода.

    # Эта функция стирает последний символ в числе, если число не пустое.
    def backspace(self):
        if self.writtenNumber == '': # Если число пустое,
            return # то мы выходим из функции.
        
        # Удаляем последний символ в числе. 
        # self.writtenNumber[:-1] получает так называемую подстроку из строки self.writtenNumber.
        # Выражение в квадратных скобках - вида [откудаНачинаетсяПодстрока:ГдеЗаканчивается].
        # Если не указано, откуда начинается подстрока, как в этом случае, то начинается она с начала строки.
        # Отрицательное значение "-x" конца подстроки означает, что нужно отступить "x" символов с конца строки.
        # В этом случае - "-1", то есть один символ с конца строки.
        # Итого: взять подстроку с начала строки self.writtenNumber до предпоследнего символа, т.е. фактически убрать последний символ.
        self.writtenNumber = self.writtenNumber[:-1] 
        self.lastWrittenNumber = self.writtenNumber # Снова сохраняем полученное число.
        self.ui.fieldLineEdit.setText(self.writtenNumber) # Показываем полученное число пользователю.

    # Обнуляет весь калькулятор, позволяя начать ввод выражения с начала.
    def clear(self):
        self.writtenNumber = ''
        self.storedNumber = 0
        self.lastWrittenNumber = 0
        self.result = 0
        self.operation = ''
        self.ui.fieldLineEdit.setText('')

    # Берёт квадратный корень из числа, введённого пользователем.
    def square_root(self):
        if self.result != 0 and self.writtenNumber == '' and self.storedNumber == 0: # Если мы только что получили результат и не вводили ничего после:
            self.result = round(sqrt(self.result), self.DECIMAL_PRECISION) # Берём корень из результата и округляем его согласно точности округления чисел.
            self.ui.fieldLineEdit.setText(str(self.result)) # Показываем полученный результат пользователю.
            return # Останавливаем дальнейшее выполнение функции.
        elif self.writtenNumber == '': # Если мы уже что-то вводили, но брать корень не из чего, так как вводимое сейчас число - пустое:
            self.ui.fieldLineEdit.setText('Enter a number at first') # Говорим пользователю сначала ввести число.
            return # Останавливаем дальнейшее выполнение функции.
        
        # Сюда мы попадаем только, если мы не округляем результат И если число, которое мы хотим округлить, не пустое:
        self.writtenNumber = str(round(sqrt(float(self.writtenNumber)), self.DECIMAL_PRECISION)) # Берём корень из введённого числа и округляем его согласно точности округления чисел.
        self.ui.fieldLineEdit.setText(self.writtenNumber) # Показываем полученное число.

    # Эта функция устанавливает операцию.
    # Тут алгоритм несколько сложнее и требует доп. объяснений. Но можно понять и так.
    def set_operation(self, operation):
        if self.writtenNumber != '' and self.storedNumber != 0: # Если оба числа введены (и, следовательно, была введена операция):
            self.calculate() # Просчитываем прошлую операцию и продолжаем эту функцию.
        elif self.writtenNumber == '' and self.result == 0: # Если мы ещё не ввели число и мы ранее не просчитывали результат:
            self.ui.fieldLineEdit.setText('Enter a number at first') # Просим сначала ввести число.
            return # Останавливаем выполнение этой функции.
        self.operation = operation # Сохраняем выбранную операцию.
        if self.writtenNumber != '': # Если мы уже ввели число:
            self.storedNumber = round(float(self.writtenNumber), self.DECIMAL_PRECISION) # Сохраняем это число, округлив его.
        elif self.result != 0: # Если мы не ввели число, но до этого вычисляли результат:
            # Это условие может выполниться только тогда, когда мы хотим продолжить вычисления, использовав результат прошлого выражения в качестве первого числа.
            self.storedNumber = self.result # Сохраняем результат в качестве первого числа в операции.
        self.writtenNumber = '' # Обнуляем переменную введённого числа, чтобы можно было ввести второе число.
        self.ui.fieldLineEdit.setText(operation) # Показываем пользователю выбранную операцию.

    # Функция, вычисляющая введённое выражение.
    def calculate(self):
        if self.storedNumber == 0 and self.writtenNumber == '' and self.result != 0: # Если мы не ввели никаких чисел:
            # Это условие используется для повторения последней операции при нажатии кнопки "=" после получения результата.
            self.storedNumber = self.result # Используем результат в качестве первого числа.
            self.writtenNumber = self.lastWrittenNumber # Используем последнее введённое число в качестве второго числа.
        if self.writtenNumber == '' and self.storedNumber != 0: # Если мы не ввели второе число:
            self.ui.fieldLineEdit.setText('Enter the second number') # Просим ввести второе число.
            return # Останавливаем выполнение функции.
        if self.operation == '+': # Если операция - сложение.
            self.result = round(self.storedNumber + float(self.writtenNumber), self.DECIMAL_PRECISION) # Складываем числа и округляем результат. 
            # self.writtenNumber - строка, так что конвертируем её в число с помощью функции float()
        elif self.operation == '-': # Если операция - вычитание.
            self.result = round(self.storedNumber - float(self.writtenNumber), self.DECIMAL_PRECISION) # Вычитаем второе число из первого числа и округляем результат. 
        elif self.operation == '*': # Если операция - умножение.
            self.result = round(self.storedNumber * float(self.writtenNumber), self.DECIMAL_PRECISION) # Перемножаем числа и округляем результат.  
        elif self.operation == ':': # Если операция - деление.
            if self.writtenNumber == '0': # Если второе число - 0:
                self.ui.fieldLineEdit.setText('Cannot divide by zero.') # На ноль делить нельзя, говорим об этом пользователю.
                return # Останавливаем выполнение функции.
            self.result = round(self.storedNumber / float(self.writtenNumber), self.DECIMAL_PRECISION) # Делим первое число на второе и округляем результат.  
        elif self.operation == '%': # Если операция - остаток от деления. 
            self.result = round(self.storedNumber % float(self.writtenNumber), self.DECIMAL_PRECISION) # Получаем остаток от деления первого числа на второе и округляем результат. 
        elif self.operation == '^': # Если операция - возведение в степень.
            self.result = round(self.storedNumber ** float(self.writtenNumber), self.DECIMAL_PRECISION) # Возводим первое число в степень второго числа и округляем результат. 
        self.storedNumber = 0 # Обнуляем первое число.
        self.writtenNumber = '' # Обнуляем второе число.
        self.ui.fieldLineEdit.setText(str(self.result)) # Показываем пользователю результат.
        
# Строки кода ниже выполняются при запуске самого приложения.
# Создаём переменную самого приложения.
app = QApplication(sys.argv)

# Создаём окно приложения.
window = MainWindow()
# Показываем это окно.
window.show()

# Сам точно не знаю, зачем это нужно, но это обязательно для корректной работы приложения.
sys.exit(app.exec())