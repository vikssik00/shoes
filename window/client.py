from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QScrollArea, QFrame, QMessageBox
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

        # Картинка
        image_label = QLabel()
        image_name = product.get("photo")  # из базы, например "9.jpg"

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

        # Информация о товаре
        info_layout = QVBoxLayout()

        title = QLabel(
            f"<b>{product['category']} | {product['name']}</b>"
        )
        info_layout.addWidget(title)

        info_layout.addWidget(QLabel(f"Описание товара: {product['description']}"))
        info_layout.addWidget(QLabel(f"Производитель: {product['producer']}"))
        info_layout.addWidget(QLabel(f"Поставщик: {product['supplier']}"))
        info_layout.addWidget(QLabel(f"Цена: {product['price']} ₽"))
        info_layout.addWidget(
            QLabel(f"Количество на складе: {product['quantity_in_stock']}")
        )

        layout.addLayout(info_layout)

        # Скидка
        discount = QLabel(f"{product['discount']}%")
        discount.setFixedWidth(60)
        discount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discount.setStyleSheet(
            "font-size: 16px; font-weight: bold;"
        )
        layout.addWidget(discount)

        # Подсветка
        if product["discount"] > 15:
            self.setStyleSheet("background-color: #2E8B57; padding: 8px;")
        elif product["quantity_in_stock"] == 0:
            self.setStyleSheet("background-color: lightblue; padding: 8px;")


class ClientWindow(QWidget):
    def __init__(self, fio):
        super().__init__()
        self.setWindowTitle("Окно клиента")
        self.resize(900, 650)

        main_layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        label_fio = QLabel(fio)
        btn_exit = QPushButton("Выйти")
        btn_exit.clicked.connect(self.logout)

        top_layout.addStretch()
        top_layout.addWidget(label_fio)
        top_layout.addWidget(btn_exit)

        main_layout.addLayout(top_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(container)

        for product in get_products():
            container_layout.addWidget(ProductCard(product))

        scroll.setWidget(container)
        main_layout.addWidget(scroll)

    def logout(self):
        # Подтверждение возврата к окну авторизации
        reply = QMessageBox.question(
            self,
            "Подтверждение выхода",
            "Вы действительно хотите выйти из аккаунта?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            from authorization import LoginWindow
            self.close()
            self.login = LoginWindow()
            self.login.show()
