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

imageItem = pg.ImageItem(img)
imageItem.setLookupTable(lut)
imageItem.setLevels([-3, 4])
view.addItem(imageItem)

colorScaleImageItem = pg.ImageItem() # image data will be set in setLut

colorScaleViewBox = pg.ViewBox(enableMenu=False, border=None)
colorScaleViewBox.disableAutoRange(pg.ViewBox.XYAxes)
colorScaleViewBox.setMouseEnabled(x=False, y=False)
colorScaleViewBox.setMinimumWidth(10)
colorScaleViewBox.setMaximumWidth(25)
colorScaleViewBox.addItem(colorScaleImageItem)
view.addItem(colorScaleViewBox)
# view.addItem(colorScaleImageItem)


# Draw a color scale that shows the LUT.
barWidth = 1
imgAxOrder = pg.getConfigOption('imageAxisOrder')
if imgAxOrder == 'col-major':
    lutImg = np.ones(shape=(barWidth, len(lut), 3), dtype=lut.dtype)
    lutImg[...] = lut[np.newaxis, :, :]
elif imgAxOrder == 'row-major':
    lutImg = np.ones(shape=(len(lut), barWidth, 3), dtype=lut.dtype)
    lutImg[...] = lut[:, np.newaxis, :]
else:
    raise AssertionError("Unexpected imageAxisOrder config value: {}".format(imgAxOrder))

colorScaleImageItem.setImage(lutImg)

yRange = [0, len(lut)]


colorScaleViewBox.setZValue(10)

# Overlay viewbox that will have alway have the same geometry as the colorScaleViewBox
overlayViewBox = pg.ViewBox(
    enableMenu=False, border=pg.mkPen(pg.getConfigOption('foreground'), width=1))
overlayViewBox.setZValue(100)

axisItem = pg.AxisItem(
    orientation='right', linkView=overlayViewBox,
    showValues=True,  parent=view)


# Overall layout
from PyQt5 import QtWidgets

mainLayout = QtWidgets.QGraphicsGridLayout()
pg_wid = pg.GraphicsWidget(parent=view)
pg_wid.setLayout(mainLayout)
mainLayout.setContentsMargins(1, 1, 1, 1)
mainLayout.setSpacing(0)
mainLayout.addItem(colorScaleViewBox, 0, 1)
# mainLayout.addItem(colorScaleImageItem, 0, 1)
mainLayout.addItem(axisItem, 0, 2)
overlayViewBox.setParentItem(colorScaleViewBox.parentItem())

colorScaleViewBox.autoRange()

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.instance().exec_()
