# -*- coding: utf-8 -*-
"""
/***************************************************************************
 skraafotosDialog
                                 A QGIS plugin
 Dette plugin laver opslag på Dataforsyningens Skråfotos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-03-21
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Morten Storm, Styrke 10 ApS
        email                : morten@styrke10.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'skraafoto_dialog_base.ui'))


class skraafotosDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(skraafotosDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        gifFile = os.path.join( os.path.dirname(__file__), "demo.gif") 
        self.movie = QMovie(gifFile)
        if self.movie.isValid():
            self.giflabel.setMovie(self.movie)
            self.movie.start()
        else:
            QgsMessageLog.logMessage('demo.gif not valid!', tag='skraafoto', level=Qgis.Warning )


