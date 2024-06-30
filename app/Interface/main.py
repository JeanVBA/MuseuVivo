# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Importando a classe gerada do arquivo .ui
from ui_functions import exibition
from interfaces import searchs, applys, initializes

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MuseuVivo - Gerenciamento")

        exibition(self)
        initializes(self)
        applys(self)
        searchs(self)
        re_initialize(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
