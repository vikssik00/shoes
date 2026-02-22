from PyQt6.QtWidgets import (
    QWidget, QPushButton,
    QVBoxLayout, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt

from queries import get_user
from window.guest import GuestWindow
from window.client import ClientWindow
from window.manager import ManagerWindow
from window.admin import AdminWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login = QLineEdit()
        self.login.setPlaceholderText("Логин")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Войти")
        btn_guest = QPushButton("Войти как гость")

        btn_login.clicked.connect(self.authorize)
        btn_guest.clicked.connect(self.open_guest)

        layout.addWidget(self.login)
        layout.addWidget(self.password)
        layout.addWidget(btn_login)
        layout.addWidget(btn_guest)

        self.setLayout(layout)

    def authorize(self):
        login = self.login.text().strip()
        password = self.password.text().strip()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка ввода", "Введите логин и пароль")
            return

        try:
            user = get_user(login, password)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка базы данных", f"Ошибка подключения к базе данных:\n{e}")
            return

        if not user:
            QMessageBox.critical(self, "Ошибка авторизации", "Неверный логин или пароль")
            return

        fio = f"{user['last_name']} {user['first_name']} {user['patronymic']}"

        self.close()

        role = user["role"]

        if role == "Авторизированный клиент":
            self.window = ClientWindow(fio)
        elif role == "Менеджер":
            self.window = ManagerWindow(fio)
        elif role == "Администратор":
            self.window = AdminWindow(fio)
        else:
            QMessageBox.warning(self, "Ошибка", "Неизвестная роль")
            return

        self.window.show()

    def open_guest(self):
        self.close()
        self.window = GuestWindow()
        self.window.show()
