import sqlite3
from PyQt6 import QtWidgets
from UI.main_ui import Ui_CoffeeApp
from UI.addEditCoffeeform_ui import Ui_AddEditCoffeeForm


class AddEditCoffeeForm(QtWidgets.QDialog, Ui_AddEditCoffeeForm):
    def __init__(self, coffee_id=None, parent=None):
        super(AddEditCoffeeForm, self).__init__(parent)
        self.setupUi(self)

        self.coffee_id = coffee_id
        if coffee_id:
            self.load_coffee_data(coffee_id)

        self.saveButton.clicked.connect(self.save_coffee)

    def load_coffee_data(self, coffee_id):
        with sqlite3.connect('data/coffee.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM coffee WHERE id=?", (coffee_id,))
            row = cursor.fetchone()
            if row:
                self.nameLineEdit.setText(row[1])
                self.roastLineEdit.setText(row[2])
                self.typeLineEdit.setText(row[3])
                self.tasteLineEdit.setText(row[4])
                self.priceLineEdit.setText(str(row[5]))
                self.volumeLineEdit.setText(row[6])

    def save_coffee(self):
        try:
            name = self.nameLineEdit.text()
            roast = self.roastLineEdit.text()
            coffee_type = self.typeLineEdit.text()
            taste = self.tasteLineEdit.text()
            price = float(self.priceLineEdit.text())
            volume = self.volumeLineEdit.text()

            with sqlite3.connect('data/coffee.sqlite') as connection:
                cursor = connection.cursor()

                if self.coffee_id:
                    cursor.execute("UPDATE coffee SET name=?, roast_level=?, type=?, taste_description=?, price=?, "
                                   "package_volume=? WHERE id=?",
                                   (name, roast, coffee_type, taste, price, volume, self.coffee_id))
                else:
                    cursor.execute(
                        "INSERT INTO coffee (name, roast_level, type, taste_description, price, package_volume) "
                        "VALUES (?, ?, ?, ?, ?, ?)",
                        (name, roast, coffee_type, taste, price, volume))

                connection.commit()
            self.accept()

        except Exception as e:
            print(f"Error saving coffee: {e}")
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось сохранить данные о кофе.")


class CoffeeApp(QtWidgets.QMainWindow, Ui_CoffeeApp):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        self.setupUi(self)
        self.load_data()

        self.addButton = QtWidgets.QPushButton("Добавить кофе", self)
        self.addButton.clicked.connect(self.add_coffee)
        self.verticalLayout.addWidget(self.addButton)

        self.editButton = QtWidgets.QPushButton("Редактировать кофе", self)
        self.editButton.clicked.connect(self.edit_coffee)
        self.verticalLayout.addWidget(self.editButton)

    def load_data(self):
        with sqlite3.connect('data/coffee.sqlite') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM coffee")
            rows = cursor.fetchall()
            self.listWidget.clear()
            for row in rows:
                self.listWidget.addItem(f"ID: {row[0]}, Название: {row[1]}, Обжарка: {row[2]}, "
                                        f"Тип: {row[3]}, Вкус: {row[4]}, Цена: {row[5]}, Объем: {row[6]}")

    def add_coffee(self):
        form = AddEditCoffeeForm(parent=self)
        if form.exec():
            self.load_data()

    def edit_coffee(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            coffee_id = int(selected_item.text().split(",")[0].split(":")[1])
            form = AddEditCoffeeForm(coffee_id=coffee_id, parent=self)
            if form.exec():
                self.load_data()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec()