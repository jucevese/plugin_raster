def name():
    return 'Raster'

def author():
    return 'Julio César Vences Serrato'

def authorName():
    return author()

def email():
    return 'jucevese@gmail.com'

def description():
    return 'Raster'

def about():
    return 'Raster'

def version():
    return '0.0.1'

def qgisMinimunVersion():
    return '3.0'

def icon():
    return 'icon.png'

def category():
    return 'Raster'

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)