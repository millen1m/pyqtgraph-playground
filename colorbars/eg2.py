import numpy as np
import pyqtgraph as pg

# build lookup table
lut = np.zeros((255,3), dtype=np.ubyte)
lut[:128,0] = np.arange(0,255,2)
lut[128:,0] = 255
lut[:,1] = np.arange(255)

# random image data
img = np.random.normal(size=(100,100))

# GUI
win = pg.GraphicsWindow()
view = win.addViewBox()
view.setAspectLocked(True)
item = pg.ImageItem(img)

item.setLookupTable(lut)
item.setLevels([0,1])
view.addItem(item)

# Equivalently, you could use a ColorMap to generate the lookup table:

# pos = np.array([0.0, 0.5, 1.0])
# color = np.array([[0,0,0,255], [255,128,0,255], [255,255,0,255]], dtype=np.ubyte)
# map = pg.ColorMap(pos, color)
# lut = map.getLookupTable(0.0, 1.0, 256)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.instance().exec_()
