# -*- coding: utf-8 -*-
"""
Very basic 3D graphics example; create a view widget and add a few items.

"""
## Add path to library (just for examples; you do not need this)

import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 10
w.show()
w.setWindowTitle('pyqtgraph example: GLViewWidget')

ax = gl.GLAxisItem()
ax.setSize(5, 5, 5)
w.addItem(ax)

x_box = [0, 1, 1, 0, 0, 1, 1, 0]
y_box = [0, 0, 1, 1, 0, 0, 1, 1]
z_box = [0, 0, 0, 0, 4, 4, 4, 4]

class SurfaceBox(object):
    def __init__(self, x_box, y_box, z_box):
        self.x_box = x_box
        self.y_box = y_box
        self.z_box = z_box

    def build_surfaces(self):  # Try build box with triangle mesh
        xb = self.x_box
        yb = self.y_box
        x = [xb[0], xb[1]]
        y = [yb[0], yb[1]]
        z = []

x = np.array([0, 1, 2, 3])
y = np.arange(3)
# z = np.arange(len(y))
z = np.ones((len(x), len(y)))
b = gl.GLSurfacePlotItem(x, y, z=z, shader='normalColor')
# b = gl.GLBoxItem(color = (255,255,255,80), glOptions='translucent')
# b.paint()
w.addItem(b)

x = np.array([0, 1, 2, 3])
y = np.ones(3) * 3
# z = np.arange(len(y))
z = np.ones((len(x), len(y))) * np.arange(len(y))[np.newaxis, :]
b = gl.GLSurfacePlotItem(x, y, z=z)
# b = gl.GLBoxItem(color = (255,255,255,80), glOptions='translucent')
# b.paint()
w.addItem(b)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
