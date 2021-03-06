# -*- coding: utf-8 -*-
"""
Very basic 3D graphics example; create a view widget and add a few items.

"""
## Add path to library (just for examples; you do not need this)

import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 10
w.show()
w.setWindowTitle('pyqtgraph example: GLViewWidget')

ax = gl.GLAxisItem()
ax.setSize(5, 5, 5)
w.addItem(ax)

b = gl.GLBoxItem(color = (255,255,255,80), glOptions='translucent')
b.paint()
w.addItem(b)

ax2 = gl.GLAxisItem()
ax2.setParentItem(b)

b.translate(1, 1, 1)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
