#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    """
    Main window class, inherits from :class: QMainWindow
    Creates the main application window
    """

    def __init__(self):
        """
        Constructor method
        """

        super().__init__()
        uic.loadUi('ui_templates/map.ui', self)

        self.setWindowIcon(QtGui.QIcon('src/logo.png'))

        self.pixmap = QPixmap()

        self.findButton.clicked.connect(self.getMapFromCoordinates)

    def getMapFromCoordinates(self):
        coords = self.coordsInput.text()
        self.pixmap.loadFromData(requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={coords}&z=4&l=sat').content)
        self.map.setPixmap(self.pixmap)