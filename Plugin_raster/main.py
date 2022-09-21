import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .raster import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle('Raster')
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar('Raster')

        self.ejemploRaster = QAction(QIcon(""),"Datos", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values() 
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType()== QgsWkbTypes.PolygonGeometry:
                vLayer = layer
            if layer.type() == QgsRasterLayer.RasterLayer:
                rLayer = layer
                self.dialogo.ui.cmb1.addItem(rLayer.name())
                epsg = rLayer.crs().authid()
                self.dialogo.ui.lb1.setText(str(epsg))
                ext = rLayer.extent()
                alto = rLayer.height()
                pixelX = rLayer.rasterUnitsPerPixelX()
                pixelY = rLayer.rasterUnitsPerPixelY()
                xmin = ext.xMinimum()
                xmax = ext.xMaximum()
                ymin = ext.yMinimum()
                ymax = ext.yMaximum()
                self.dialogo.ui.txEdt.setText('Coordenadas: \n' + str(ext) +
                                              '\nAltura: \n' + str(alto) + 
                                              '\nTamaño pixel X: \n' + str(pixelX) +
                                              '\nTamaño pixel Y: \n' + str(pixelY) +
                                              '\nX Min: \n' + str(xmin) +
                                              '\nX Max: \n' + str(xmax) + 
                                              '\nY Min: \n' + str(ymin) +
                                              '\nY Max: \n' + str(ymax))
    def unload(self):
            QgsApplication.processingRegistry().removeProvider(self.provider)
