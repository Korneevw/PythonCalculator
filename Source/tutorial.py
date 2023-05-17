# Использованные материалы:
# 1. https://www.pythontutorial.net/pyqt/qt-designer/ - использование QtDesigner с Python кодом.
# 2. https://learn.microsoft.com/ru-ru/training/modules/introduction-to-github-visual-studio-code/1-introduction - использование GitHub в VSCode.
# 3. https://habr.com/ru/companies/skillfactory/articles/599599/ - общий гайд по PyQt6.

# Получение доступа к виджетам из PyQt6 в коде.
from PyQt6.QtWidgets import (QApplication, QMainWindow)

# Импорт интерфейса из Python файла, полученного конвертацией .ui файла в код Python с помощью консольной команды:
# "pyuic -o calculator_ui.py calculator_new.ui", где calculator_ui.py - Python файл, куда нужно сгенерировать код,
# calculator_new.ui - файл интерфейса из QtDesigner.
from calculator_ui import Ui_TheNamelessCalculator

# Необходимо для строчки "app = QApplication(sys.argv)".
import sys

class MainWindow(QMainWindow):

    # Эта функция вызывается при создании объекта этого окна (строчка "window = MainWindow()").
    def __init__(self):
        # Позволяем сначала инициализироваться базовому классу (QMainWindow) по иерархии наследования.
        super().__init__()

        # Создаём переменную для сгенерированного интерфейса (Python файл, calculator_ui.pu) в этом классе.
        self.ui = Ui_TheNamelessCalculator()
        # Вызываем функцию инициализации.
        self.ui.setupUi(self)

        # Обращаемся к кнопке, отвечающей за единицу "oneButton" через переменную интерфейса "ui",
        # и у неё есть сигнал клика по ней (абзац "Слоты и Сигналы" в гайде №3), к которому мы привязываем "слот",
        # представленный функцией "button_clicked". Слоты реагируют на сигналы и выполняют определённые действия в ответ.
        # Сейчас эта строчка и метод "button_clicked" не несёт функционала калькулятора и сделана просто для практики.
        # 
        # Теперь при нажатии кнопки единицы в консоль пишется "Clicked!". 
        self.ui.oneButton.clicked.connect(self.button_clicked)
        # Делаем кнопку "переключаемой". Тоже из туториала №3.
        self.ui.oneButton.setCheckable(True)
        # То же самое, что и с кликом, только уже обрабатывается переключение кнопки.
        self.ui.oneButton.toggled.connect(self.button_toggled)
        
        # Устанавливаем название окна приложения.
        self.setWindowTitle('The Nameless Calculator')

    def button_clicked(self):
        print('Clicked!')

    # В этот слот сама кнопка может передавать данные. В этом случае - её состояние, переключена она или нет.
    # Служит примером обработки сигналов, передающих данные. Туториал №3.
    def button_toggled(self, toggled):
        print('Toggled? ', toggled)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Создаём объект класса MainWindow, определённого выше.
    window = MainWindow()
    # Показываем окно приложения.
    window.show()

    sys.exit(app.exec())