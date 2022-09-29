import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from osgeo import gdal, osr

from .raster import interfaz

class mainMenu:
    def __init__(self,iface):
        self.iface = iface

    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.IMenu)
        self.IMenuBar = self.iface.addToolBar("Raster")
        
        self.ejemplo = QAction(QIcon(""), "Raster", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemplo)
        self.ejemplo.triggered.connect(self.startInterfaz)

    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QgsWkbTypes.PolygonGeometry: 
                vlayer = layer
            if layer.type() == QgsRasterLayer.RasterLayer:
                rlayer = layer
                self.dialogo.ui.cmb1.addItem(rlayer.name())
                epsg=rlayer.crs()
                self.dialogo.ui.lb1.setText(str(epsg.authid()))
                ext = rlayer.extent().toString()
                ymin = str(rlayer.extent().yMinimum())
                ymax = str(rlayer.extent().yMaximum())
                xmin = str(rlayer.extent().xMinimum())
                xmax = str(rlayer.extent().xMaximum())
                Ancho = str(rlayer.width())
                Alto = str(rlayer.height())
                bandas = str(rlayer.bandCount())
                pixelx = str(rlayer.rasterUnitsPerPixelX())
                pixely = str(rlayer.rasterUnitsPerPixelY())
                self.dialogo.ui.textEdit.setText(str("Exntesión de la capa: " +ext +"\nY Mínima: "+ymin+
                "\nY Máxima: "+ymax+"\nX Mínima: "+xmin+"\nX Máxima: "+xmax+"\nAncho: "+Ancho+"\nAlto: "+Alto+
                "\nNúmero de bandas: "+bandas+"\nTamaño Pixel x: "+pixelx+"\nTamaño Pixel y: "+pixely))
        
    def unload(self):
            self.IMenu.deleteLater()
            #QgsApplication.processingGuiRegistry().removeProvider(self.provider)

