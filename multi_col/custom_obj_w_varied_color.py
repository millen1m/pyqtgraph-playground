"""
Demonstrate creation of a custom graphic (a candlestick plot)

"""
# import initExample ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import numpy as np


## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect()
## (see QGraphicsItem documentation)
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, xdat, ydat, connect):
        pg.GraphicsObject.__init__(self)
        self.xdat = xdat
        self.ydat = ydat
        self.connect = connect
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly,
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        for i in range(int(len(self.xdat) / 5)):
            print(self.xdat[i*5:(i+1) * 5], self.ydat[i*5:(i+1) * 5])
            self.path = pg.arrayToQPath(self.xdat[i * 5:(i+1) * 5], self.ydat[i * 5:(i+1) * 5])
            # self.path = pg.arrayToQPath(np.array([0, 1, 1, 0, 3, 1]), np.array([0, 0, 1, 1, 3, 1]))
            p2 = QtGui.QPainterPath(self.path)
            p.fillPath(p2, pg.mkBrush((100, 100, 10 + i * 10)))

        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

def run():
    x_all = []
    y_all = []
    c_all = []
    for j in range(10):
        x = np.array([0, 1, 1, 0, 0]) + j
        y = np.array([0, 0, 1, 1, 0]) + j
        connect = np.array([1, 1, 1, 1, 0])
        x_all.append(x)
        y_all.append(y)
        c_all.append(connect)
    x_all = np.array(x_all).flatten()
    y_all = np.array(y_all).flatten()
    c_all = np.array(c_all).flatten()
    item = CandlestickItem(x_all, y_all, c_all)
    plt = pg.plot()
    plt.addItem(item)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if __name__ == '__main__':
        import sys

        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    run()