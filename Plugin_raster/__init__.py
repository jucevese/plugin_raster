def name():
    return "Raster"

def author():
    return "Héctor Solares Hernández"

def authorName():
    return author()

def email():
    return "solares.hec@gmail.com"

def description():
    return "raster"

def about():
    return "Raster"

def version():
    return "0.0.1"

def qgisMinimumVersion():
    return "3.0"

def icon():
    return "raster.png"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)