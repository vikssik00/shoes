from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QScrollArea, QFrame, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from queries import get_orders
from window.order_form import OrderForm

class OrderCard(QFrame):
    def __init__(self, order, is_admin=False, parent=None):
        super().__init__()
        self.parent_window = parent
        self.setFrameShape(QFrame.Shape.Box)

        main_layout = QHBoxLayout(self)
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel(f"<b>Артикул заказа:</b> {order['code']}"))
        left_layout.addWidget(QLabel(f"Статус заказа: {order['status']}"))
        left_layout.addWidget(QLabel(f"Адрес пункта выдачи: {order['address']}"))
        left_layout.addWidget(QLabel(f"Дата заказа: {order['order_date']}"))
        main_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        delivery_label = QLabel(f"Дата доставки:\n{order['delivery_date']}")
        delivery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        delivery_label.setFixedWidth(150)
        delivery_label.setStyleSheet("border: 1px solid black; padding: 5px;")
        right_layout.addWidget(delivery_label)
        main_layout.addLayout(right_layout)

        if is_admin:
            # Открытие формы редактирования при клике на карточку
            self.mousePressEvent = lambda e, c=order['code']: self.parent_window.open_edit_form(c)

class OrderWindow(QWidget):
    def __init__(self, user_id=None, is_admin=False):
        super().__init__()
        self.setWindowTitle("Список заказов")
        self.resize(800, 600)
        self.is_admin = is_admin
        self.user_id = user_id
        self.edit_window = None

        main_layout = QVBoxLayout(self)

        if is_admin:
            btn_add = QPushButton("Добавить заказ")
            btn_add.clicked.connect(self.open_add_form)
            main_layout.addWidget(btn_add)

        # ScrollArea для списка заказов
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.scroll.setWidget(self.container)
        main_layout.addWidget(self.scroll)

        self.refresh_orders()

    def refresh_orders(self):
        orders = get_orders()

        # Очищаем старые карточки
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Создаем карточки заказов
        for order in orders:
            card = OrderCard(order, self.is_admin, parent=self)
            self.container_layout.addWidget(card)

    # Открытие формы добавления
    def open_add_form(self):
        if self.edit_window:
            QMessageBox.warning(self, "Окно уже открыто", "Форма редактирования уже открыта.")
            return
        self.edit_window = OrderForm(self, mode="add", user_id=self.user_id)
        self.edit_window.show()

    # Открытие формы редактирования
    def open_edit_form(self, code):
        if self.edit_window:
            QMessageBox.warning(self, "Окно уже открыто", "Форма редактирования уже открыта.")
            return
        self.edit_window = OrderForm(self, mode="edit", code=code)
        self.edit_window.show()