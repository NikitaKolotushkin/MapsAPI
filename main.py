#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())