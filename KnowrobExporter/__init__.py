# -*- coding: utf-8 -*-
"""
/***************************************************************************
 KnowrobExporter
                                 A QGIS plugin
 This is KnowrobExporter
                             -------------------
        begin                : 2014-12-08
        copyright            : (C) 2014 by IAI Bremen
        email                : bbrieber@cs.uni-bremen.de
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
    """Load KnowrobExporter class from file KnowrobExporter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_knowrob_exporter import KnowrobExporter
    return KnowrobExporter(iface)
