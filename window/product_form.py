import os
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout,
    QPushButton, QFileDialog, QMessageBox,
    QComboBox, QSpinBox, QDoubleSpinBox
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from queries import (
    get_categories, get_producers, get_suppliers,
    get_product_by_article,
    add_product, update_product,
    delete_product, product_in_order,
    get_next_article
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")


class ProductForm(QWidget):
    def __init__(self, parent, mode="add", article=None):
        super().__init__()
        self.parent = parent
        self.mode = mode
        self.article = article
        self.image_path = None
        self.old_image = None

        self.setWindowTitle("Добавление товара" if mode == "add" else "Редактирование товара")
        self.setFixedSize(400, 650)

        layout = QVBoxLayout(self)

        # Фото
        self.image_label = QLabel()
        self.image_label.setFixedSize(300, 200)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load_placeholder()

        btn_image = QPushButton("Выбрать фото")
        btn_image.clicked.connect(self.choose_image)

        layout.addWidget(self.image_label)
        layout.addWidget(btn_image)

        # Article
        self.article_input = QLineEdit()
        self.article_input.setReadOnly(mode == "edit")
        layout.addWidget(self.article_input)

        # Название
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Название")
        layout.addWidget(self.name_input)

        # Категория
        self.category_combo = QComboBox()
        for c in get_categories():
            self.category_combo.addItem(c["name"], c["id"])
        layout.addWidget(self.category_combo)

        # Описание
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Описание")
        layout.addWidget(self.desc_input)

        # Производитель
        self.producer_combo = QComboBox()
        for p in get_producers():
            self.producer_combo.addItem(p["name"], p["id"])
        layout.addWidget(self.producer_combo)

        # Поставщик
        self.supplier_combo = QComboBox()
        for s in get_suppliers():
            self.supplier_combo.addItem(s["name"], s["id"])
        layout.addWidget(self.supplier_combo)

        # Цена
        self.price_input = QDoubleSpinBox()
        self.price_input.setMinimum(0)
        self.price_input.setMaximum(999999.99)
        self.price_input.setDecimals(2)
        layout.addWidget(self.price_input)

        # Ед. измерения
        self.unit_input = QLineEdit()
        self.unit_input.setPlaceholderText("Ед. измерения")
        layout.addWidget(self.unit_input)

        # Количество
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(0)
        layout.addWidget(self.quantity_input)

        # Скидка
        self.discount_input = QSpinBox()
        self.discount_input.setMinimum(0)
        self.discount_input.setMaximum(100)
        layout.addWidget(self.discount_input)

        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save_product)
        layout.addWidget(btn_save)

        if mode == "edit":
            btn_delete = QPushButton("Удалить")
            btn_delete.clicked.connect(self.remove_product)
            layout.addWidget(btn_delete)

        if mode == "add":
            self.article_input.setText(get_next_article())

        if mode == "edit":
            self.load_data()

    # Фото
    def load_placeholder(self):
        path = os.path.join(IMAGES_DIR, "picture.png")
        if os.path.exists(path):
            pixmap = QPixmap(path).scaled(
                300, 200,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)

    def choose_image(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Выбрать изображение", "", "Images (*.png *.jpg *.jpeg)"
        )
        if file:
            pixmap = QPixmap(file).scaled(
                300, 200,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)
            self.image_path = file

    # Загрузка
    def load_data(self):
        product = get_product_by_article(self.article)

        self.article_input.setText(product["article"])
        self.name_input.setText(product["name"])
        self.desc_input.setText(product["description"])
        self.price_input.setValue(float(product["price"]))
        self.unit_input.setText(product["unit_of_measurement"])
        self.quantity_input.setValue(product["quantity_in_stock"])
        self.discount_input.setValue(product["discount"])

        self.old_image = product["photo"]

        if self.old_image:
            image_path = os.path.join(IMAGES_DIR, self.old_image)
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path).scaled(
                    300, 200,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_label.setPixmap(pixmap)

    # Сохранение
    def save_product(self):
        if not self.name_input.text():
            QMessageBox.warning(self, "Ошибка", "Введите название")
            return

        article = self.article_input.text()
        image_filename = self.old_image or ""

        if self.image_path:
            extension = os.path.splitext(self.image_path)[1]
            image_filename = f"{article}{extension}"
            save_path = os.path.join(IMAGES_DIR, image_filename)

            pixmap = QPixmap(self.image_path).scaled(
                300, 200,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            pixmap.save(save_path)

            # Удаление старого фото
            if self.old_image and self.old_image != image_filename:
                old_path = os.path.join(IMAGES_DIR, self.old_image)
                if os.path.exists(old_path):
                    os.remove(old_path)

        data = (
            article,
            self.name_input.text(),
            self.desc_input.text(),
            str(self.price_input.value()),
            self.unit_input.text(),
            self.quantity_input.value(),
            self.discount_input.value(),
            image_filename,
            self.producer_combo.currentData(),
            self.supplier_combo.currentData(),
            self.category_combo.currentData()
        )

        if self.mode == "add":
            add_product(data)
        else:
            update_product(article, data[1:])

        self.parent.refresh_products()
        self.close()

    # Удаление

    def remove_product(self):
        if product_in_order(self.article):
            QMessageBox.warning(self, "Ошибка", "Товар используется в заказе")
            return

        if self.old_image:
            image_path = os.path.join(IMAGES_DIR, self.old_image)
            if os.path.exists(image_path):
                os.remove(image_path)

        delete_product(self.article)
        self.parent.refresh_products()
        self.close()

    def closeEvent(self, event):
        self.parent.edit_window = None
        event.accept()
