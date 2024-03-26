from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QGridLayout, QLabel, QMessageBox


class Dialog(QDialog):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить запись")

        # Создаем поля ввода для каждого столбца таблицы
        self.name_line = QLineEdit()
        self.quantity_line = QLineEdit()
        self.cost_line = QLineEdit()

        # Создаем кнопки "Сохранить" и "Отмена"
        self.add_button = QPushButton("Добавить")
        self.cancel_button = QPushButton("Отмена")
        self.add_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # Создаем сетку для размещения элементов управления
        layout = QGridLayout()
        layout.addWidget(QLabel("Название:"), 1, 0)
        layout.addWidget(self.name_line, 1, 1)
        layout.addWidget(QLabel("Кол-во:"), 2, 0)
        layout.addWidget(self.quantity_line, 2, 1)
        layout.addWidget(QLabel("Цена:"), 3, 0)
        layout.addWidget(self.cost_line, 3, 1)
        layout.addWidget(self.add_button, 4, 0)
        layout.addWidget(self.cancel_button, 4, 1)

        self.setLayout(layout)

    def accept(self):
        try:
            if self.name_line.text() == '' or self.quantity_line.text() == '' or self.cost_line.text() == '':
                raise ValueError("Введите все значения")
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))
            return
        super().accept()

    def get_data(self):
        name = self.name_line.text()
        quantity = self.quantity_line.text()
        cost = self.cost_line.text()
        return name, quantity, cost
