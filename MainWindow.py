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

        self.map_types = {'Схема': 'map', 'Спутник': 'sat', 'Гибрид': 'sat,skl'}

        self.findButton.clicked.connect(self.find)
        self.mapTypeBox.currentTextChanged.connect(self.getMapFromCoordinates)

        self.long_size = 0.016457
        self.lat_size = 0.00619

    def find(self):
        self.coords = self.coordsInput.text()
        self.getMapFromCoordinates()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            print('zoom in')
            self.zoom_in()
        elif event.key() == Qt.Key_PageDown:
            print('zoom out')
            self.zoom_out()
        elif event.key() == Qt.Key_Left:
            self.move_(-1, 0)
        elif event.key() == Qt.Key_Right:
            self.move_(1, 0)
        elif event.key() == Qt.Key_Up:
            self.move_(0, 1)
        elif event.key() == Qt.Key_Down:
            self.move_(0, -1)

    def zoom_in(self):
        self.long_size *= 0.666666
        self.lat_size *= 0.666666
        self.getMapFromCoordinates()

    def zoom_out(self):
        self.long_size *= 1.5
        self.lat_size *= 1.5
        self.getMapFromCoordinates()

    def move_(self, dx, dy):
        x, y = list(map(float, self.coords.split(',')))
        x += self.long_size * 0.5 * dx
        y += self.lat_size * 0.5 * dy
        x = "{0:.6f}".format(x)
        y = "{0:.6f}".format(y)
        self.coords = str(x) + ',' + str(y)
        self.getMapFromCoordinates()

    def getMapFromCoordinates(self):
        self.map_type = self.mapTypeBox.currentText()
        self.map_type = self.map_types[self.map_type]
        self.pixmap.loadFromData(requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={self.coords}&spn={self.long_size},{self.lat_size}&l={self.map_type}').content)
        self.map.setPixmap(self.pixmap)

