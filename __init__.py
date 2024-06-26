# -*- coding: utf-8 -*-
"""
/***************************************************************************
 skraafotos
                                 A QGIS plugin
 Dette plugin laver opslag på Dataforsyningens Skråfotos
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-03-21
        copyright            : (C) 2024 by Morten Storm, Styrke 10 ApS
        email                : morten@styrke10.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load skraafotos class from file skraafotos.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .skraafoto import skraafotos
    return skraafotos(iface)
