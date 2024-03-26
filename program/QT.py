import datetime
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from form import Ui_MainWindow
from Dialog import Dialog


class InventoryApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_connection()
        self.create_table()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Учет товаров')

        self.product_name.textChanged.connect(self.onTextChanged)
        self.add_button.clicked.connect(self.add_product)

        self.product_list.setColumnCount(4)
        self.product_list.setHorizontalHeaderLabels(['ID', 'Название', 'Кол-во', 'Стоимость'])
        self.product_list.setColumnWidth(0, 50)
        self.product_list.setColumnWidth(1, 250)
        self.product_list.setColumnWidth(2, 100)
        self.product_list.setColumnWidth(3, 250)
        self.product_list.cellChanged.connect(self.update_base)
        # self.product_list.horizontalHeader().sectionClicked.connect(self.onHeaderClicked)
        self.product_list.setSortingEnabled(True)
        self.load_data()
        self.delete_btn.clicked.connect(self.delete_product)

    def create_connection(self):
        self.conn = sqlite3.connect('../products.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            quantity INTEGER,
                            cost REAL
                            )''')
        self.conn.commit()

    def load_data(self):
        self.cur.execute('''SELECT * FROM products''')
        products = self.cur.fetchall()
        self.product_list.setRowCount(0)
        for row_number, row_data in enumerate(products):
            self.product_list.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.product_list.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def update_base(self, row, column):

        id = int(self.product_list.item(row, 0).text())
        data = self.product_list.item(row, column).text()

        if column > 1:
            data = float(data)
            if data < 0:
                QMessageBox.warning(self, "Ошибка", "Неверное значение")
                self.load_data()
                return

        if column == 1: self.cur.execute("Update products set name=? where id=?", (data, id))
        if column == 2: self.cur.execute("Update products set quantity=? where id=?", (data, id))
        if column == 3: self.cur.execute("Update products set cost=? where id=?", (data, id))

        self.conn.commit()

    def delete_product(self):
        selected_rows = []
        for item in self.product_list.selectedItems():
            if item.row() not in selected_rows:
                selected_rows.append(item.row())

        try:
            for row in selected_rows:
                id = int(self.product_list.item(row, 0).text())
                self.cur.execute(f'''DELETE from products where id = {id}''')
                self.conn.commit()

            self.load_data()
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Не удалось удалить элементы')

    def add_product(self):
        dialog = Dialog(None, self)
        if dialog.exec_():
            l_name, l_quantity, l_cost = dialog.get_data()

            if l_name == '' or l_quantity == '' or l_cost == '':
                QMessageBox.information(self, 'Error', 'Введите все данные')

            try:

                name = l_name
                quantity = int(l_quantity)
                cost = float(l_cost)
                if quantity < 0:
                    QMessageBox.warning(self, "Ошибка", "Неверное количество")
                    return

                if cost < 0:
                    QMessageBox.warning(self, "Ошибка", "Неверная цена")
                    return

                self.cur.execute('''INSERT INTO products (name, quantity, cost) 
                                                VALUES (?, ?, ?)''',
                                 (name, quantity, cost))
                self.conn.commit()
                self.load_data()
            except ValueError:
                QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите корректные даннын')

    def onTextChanged(self):
        value = self.product_name.text()
        items = self.product_list.findItems(value, QtCore.Qt.MatchStartsWith)
        if items:
            item = items[0]
            self.product_list.scrollToItem(item, QAbstractItemView.EnsureVisible)
            item.setSelected(True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
