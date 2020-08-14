import numpy as np
import pyqtgraph as pg
from bwplot import cbox
from pyqtgraph.Qt import QtGui, QtCore

plt = pg.plot()
plt.setWindowTitle('pyqtgraph example: Legend')
plt.addLegend()

for i in range(100):
    x = np.array([3, 5, 5, 3, 3, 7, 9, 9, 7, 7, 7]) + i
    y = [2, 2, 4, 4, 2, 6, 6, 7, 7, 6, 6]
    connect = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0])

    pen = 'w'
    brush = pg.mkBrush(cbox(0, as255=True, alpha=80))

    # c = plt.plot(x, y, pen='w', connect=connect, fillBrush=brush, fillLevel='enclosed', name="fillLevel='enclosed'")
    # item = pg.PlotDataItem(x, y, pen='w', connect=connect, fillBrush=brush, fillLevel='enclosed', name="fillLevel='enclosed'")
    item = pg.GraphicsObject
    item.yData = y
    item.xData = x
    item.z
    plt.addItem(item, params={})

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
