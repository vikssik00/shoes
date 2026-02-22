import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from authorization import LoginWindow

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setFont(QFont("Times New Roman"))
        app.setWindowIcon(QIcon("resources/Icon.JPG"))
        window = LoginWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QMessageBox.critical(None, "Критическая ошибка", f"Ошибка запуска приложения:\n{e}")