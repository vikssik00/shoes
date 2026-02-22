from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout,
    QPushButton, QComboBox, QMessageBox, QDateEdit
)
from PyQt6.QtCore import Qt, QDate
from queries import (
    get_order_by_code, add_order, update_order,
    delete_order, get_points_of_issue
)

class OrderForm(QWidget):
    def __init__(self, parent, mode="add", code=None, user_id=None):
        super().__init__()
        self.parent = parent
        self.mode = mode
        self.code = code
        self.user_id = user_id  # id администратора, создающего заказ

        self.setWindowTitle("Добавление заказа" if mode=="add" else "Редактирование заказа")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout(self)

        # Артикул заказа
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Артикул заказа")
        self.code_input.setReadOnly(mode=="edit")
        layout.addWidget(QLabel("Артикул заказа:"))
        layout.addWidget(self.code_input)

        # Статус
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Новый", "Завершен"])
        layout.addWidget(QLabel("Статус заказа:"))
        layout.addWidget(self.status_combo)

        # Адрес пункта выдачи
        self.point_combo = QComboBox()
        self.points = get_points_of_issue()
        for p in self.points:
            self.point_combo.addItem(p["address"], p["id"])
        layout.addWidget(QLabel("Адрес пункта выдачи:"))
        layout.addWidget(self.point_combo)

        # Дата заказа
        self.order_date = QDateEdit()
        self.order_date.setCalendarPopup(True)
        self.order_date.setDate(QDate.currentDate())
        layout.addWidget(QLabel("Дата заказа:"))
        layout.addWidget(self.order_date)

        # Дата выдачи
        self.delivery_date = QDateEdit()
        self.delivery_date.setCalendarPopup(True)
        self.delivery_date.setDate(QDate.currentDate())
        layout.addWidget(QLabel("Дата выдачи:"))
        layout.addWidget(self.delivery_date)

        # Кнопки
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save_order)
        layout.addWidget(btn_save)

        if mode=="edit":
            btn_delete = QPushButton("Удалить")
            btn_delete.clicked.connect(self.remove_order)
            layout.addWidget(btn_delete)

        # Если режим редактирования, загружаем данные
        if mode=="edit" and code:
            self.load_data()

    # Загрузка данных
    def load_data(self):
        order = get_order_by_code(self.code)
        if order:
            self.code_input.setText(order["code"])
            self.status_combo.setCurrentText(order["status"])
            # Выбираем адрес
            for i, p in enumerate(self.points):
                if p["id"] == order["id_point_of_issue"]:
                    self.point_combo.setCurrentIndex(i)
                    break
            self.order_date.setDate(QDate.fromString(str(order["order_date"]), "yyyy-MM-dd"))
            self.delivery_date.setDate(QDate.fromString(str(order["delivery_date"]), "yyyy-MM-dd"))

    # Сохранение заказа
    def save_order(self):
        code = self.code_input.text().strip()
        status = self.status_combo.currentText()
        point_id = self.point_combo.currentData()
        order_date = self.order_date.date().toString("yyyy-MM-dd")
        delivery_date = self.delivery_date.date().toString("yyyy-MM-dd")

        if not code:
            QMessageBox.warning(self, "Ошибка", "Введите артикул заказа")
            return

        if self.mode=="add":
            add_order((code, status, point_id, order_date, delivery_date, self.user_id))
        else:
            update_order(code, (status, point_id, order_date, delivery_date))

        self.parent.refresh_orders()
        self.close()

    # Удаление заказа
    def remove_order(self):
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            "Вы действительно хотите удалить этот заказ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            delete_order(self.code)
            self.parent.refresh_orders()
            self.close()

    # Закрытие формы
    def closeEvent(self, event):
        self.parent.edit_window = None
        event.accept()