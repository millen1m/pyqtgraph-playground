#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ViewBox is the general-purpose graphical container that allows the user to
zoom / pan to inspect any area of a 2D coordinate system.

This unimaginative example demonstrates the constrution of a ViewBox-based
plot area with axes, very similar to the way PlotItem is built.
"""

## Add path to library (just for examples; you do not need this)

import numpy as np
lut = np.zeros((255,3), dtype=np.ubyte)
lut[:128,0] = np.arange(0,255,2)
lut[128:,0] = 255
lut[:,1] = np.arange(255)

## This example uses a ViewBox to create a PlotWidget-like interface

import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: ViewBox')
mw.show()
mw.resize(800, 600)

gv = pg.GraphicsView()
mw.setCentralWidget(gv)
l = QtGui.QGraphicsGridLayout()
l.setHorizontalSpacing(0)
l.setVerticalSpacing(0)

colorScaleViewBox = pg.ViewBox(enableMenu=False, border=None)

p1 = pg.PlotDataItem()
colorScaleViewBox.addItem(p1)


colorScaleImageItem = pg.ImageItem() # image data will be set in setLut


colorScaleViewBox.disableAutoRange(pg.ViewBox.XYAxes)
colorScaleViewBox.setMouseEnabled(x=False, y=False)
colorScaleViewBox.setMinimumWidth(10)
colorScaleViewBox.setMaximumWidth(25)
colorScaleViewBox.addItem(colorScaleImageItem)


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



l.addItem(colorScaleViewBox, 0, 1)
gv.centralWidget.setLayout(l)

xScale = pg.AxisItem(orientation='bottom', linkView=colorScaleViewBox)
l.addItem(xScale, 1, 1)
yScale = pg.AxisItem(orientation='left', linkView=colorScaleViewBox)
l.addItem(yScale, 0, 0)

xScale.setLabel(text="<span style='color: #ff0000; font-weight: bold'>X</span> <i>Axis</i>", units="s")
yScale.setLabel('Y Axis', units='V')


def rand(n):
    data = np.random.random(n)
    data[int(n * 0.1):int(n * 0.13)] += .5
    data[int(n * 0.18)] += 2
    data[int(n * 0.1):int(n * 0.13)] *= 5
    data[int(n * 0.18)] *= 20
    return data, np.arange(n, n + len(data)) / float(n)


def updateData():
    yd, xd = rand(10000)
    p1.setData(y=yd, x=xd)


yd, xd = rand(10000)
updateData()
colorScaleViewBox.autoRange()

t = QtCore.QTimer()
t.timeout.connect(updateData)
t.start(50)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
