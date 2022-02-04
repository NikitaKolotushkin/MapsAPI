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

        self.z = 4

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.zoom_in()
        elif event.key() == Qt.Key_PageDown:
            self.zoom_out()

    def zoom_in(self):
        self.z += 1
        if self.z > 19:
            self.z = 19
        self.getMapFromCoordinates()

    def zoom_out(self):
        self.z -= 1
        if self.z < 1:
            self.z = 1
        self.getMapFromCoordinates()

    def getMapFromCoordinates(self):
        coords = self.coordsInput.text()
        self.pixmap.loadFromData(requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={coords}&z={self.z}&l=sat').content)
        self.map.setPixmap(self.pixmap)