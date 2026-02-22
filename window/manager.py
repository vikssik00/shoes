from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QScrollArea, QFrame,
    QLineEdit, QComboBox, QMessageBox
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from queries import get_products
import os

IMAGE_DIR = "C:/Users/lulun/OneDrive/Рабочий стол/images"

class ProductCard(QFrame):
    def __init__(self, product):
        super().__init__()

        layout = QHBoxLayout(self)
        self.setStyleSheet("padding: 8px;")

        image_label = QLabel()
        image_name = product.get("photo")
        # Загрузка картинки или заглушки
        if image_name:
            full_path = os.path.join(IMAGE_DIR, image_name)
            if os.path.exists(full_path):
                pixmap = QPixmap(full_path)
            else:
                pixmap = QPixmap(os.path.join(IMAGE_DIR, "picture.png"))
        else:
            pixmap = QPixmap(os.path.join(IMAGE_DIR, "picture.png"))

        pixmap = pixmap.scaled(
            90, 90,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        image_label.setPixmap(pixmap)
        image_label.setFixedSize(100, 100)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)

        info_layout = QVBoxLayout()
        info_layout.addWidget(
            QLabel(f"<b>{product['category']} | {product['name']}</b>")
        )
        info_layout.addWidget(QLabel(f"Описание: {product['description']}"))
        info_layout.addWidget(QLabel(f"Производитель: {product['producer']}"))
        info_layout.addWidget(QLabel(f"Поставщик: {product['supplier']}"))
        info_layout.addWidget(QLabel(f"Цена: {product['price']} ₽"))
        info_layout.addWidget(
            QLabel(f"Количество: {product['quantity_in_stock']}")
        )

        layout.addLayout(info_layout)

        discount = QLabel(f"{product['discount']}%")
        discount.setFixedWidth(60)
        discount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discount.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(discount)

        if product["discount"] > 15:
            self.setStyleSheet("background-color: #2E8B57; padding: 8px;")
        elif product["quantity_in_stock"] == 0:
            self.setStyleSheet("background-color: lightblue; padding: 8px;")

class ManagerWindow(QWidget):
    def __init__(self, fio):
        super().__init__()
        self.setWindowTitle("Окно менеджера")
        self.resize(1000, 700)

        try:
            self.products = get_products()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка загрузки данных",
                f"Не удалось загрузить товары:\n\n{e}\n\n"
                "Проверьте подключение к базе данных."
            )
            self.products = []

        self.filtered_products = self.products.copy()

        main_layout = QVBoxLayout(self)

        # Панель фильтрации
        top_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск...")

        self.sort_combo = QComboBox()
        self.sort_combo.addItems([
            "Без сортировки",
            "Количество ↑",
            "Количество ↓"
        ])

        self.supplier_combo = QComboBox()
        self.supplier_combo.addItem("Все поставщики")
        suppliers = sorted(set(p["supplier"] for p in self.products))
        self.supplier_combo.addItems(suppliers)

        top_layout.addWidget(self.search_input)
        top_layout.addWidget(self.sort_combo)
        top_layout.addWidget(self.supplier_combo)

        main_layout.addLayout(top_layout)

        btn_orders = QPushButton("Заказы")
        btn_orders.clicked.connect(self.open_orders)
        main_layout.addWidget(btn_orders)

        # Прокручиваемая область товаров
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)

        self.scroll.setWidget(self.container)
        main_layout.addWidget(self.scroll)

        # Нижняя панель
        bottom_layout = QHBoxLayout()

        label_fio = QLabel(fio)
        label_fio.setAlignment(Qt.AlignmentFlag.AlignRight)

        btn_exit = QPushButton("Выйти")
        btn_exit.clicked.connect(self.logout)

        bottom_layout.addWidget(label_fio)
        bottom_layout.addStretch()
        bottom_layout.addWidget(btn_exit)

        main_layout.addLayout(bottom_layout)

        # Подключение фильтров
        self.search_input.textChanged.connect(self.apply_filters)
        self.sort_combo.currentIndexChanged.connect(self.apply_filters)
        self.supplier_combo.currentIndexChanged.connect(self.apply_filters)

        self.update_products_view()

    def apply_filters(self):
        search_text = self.search_input.text().lower()
        selected_supplier = self.supplier_combo.currentText()
        sort_option = self.sort_combo.currentText()

        filtered = []

        for product in self.products:

            if selected_supplier != "Все поставщики":
                if product["supplier"] != selected_supplier:
                    continue

            searchable_text = " ".join([
                str(product["name"]),
                str(product["description"]),
                str(product["producer"]),
                str(product["supplier"]),
                str(product["category"])
            ]).lower()

            if search_text not in searchable_text:
                continue

            filtered.append(product)

        if sort_option == "Количество ↑":
            filtered.sort(key=lambda x: x["quantity_in_stock"])
        elif sort_option == "Количество ↓":
            filtered.sort(key=lambda x: x["quantity_in_stock"], reverse=True)

        self.filtered_products = filtered
        self.update_products_view()

        if not filtered:
            QMessageBox.information(
                self,
                "Результат поиска",
                "По заданным параметрам товары не найдены."
            )

    def open_orders(self):
        from order import OrderWindow
        self.order_window = OrderWindow(is_admin=False)
        self.order_window.show()

    def update_products_view(self):
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for product in self.filtered_products:
            self.container_layout.addWidget(ProductCard(product))

    def logout(self):
        reply = QMessageBox.question(
            self,
            "Подтверждение выхода",
            "Вы действительно хотите выйти из учетной записи менеджера?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            from authorization import LoginWindow
            self.close()
            self.login = LoginWindow()
            self.login.show()
