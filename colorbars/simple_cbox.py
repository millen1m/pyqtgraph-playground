
import pyqtgraph as pg
import numpy as np


class ColorLegendItem(pg.GraphicsWidget):
    # Color scale
    def __init__(self,
             lut=None,
             label=None,
             showHistogram=True,
             subsampleStep='auto',
             histHeightPercentile=99.0,
             maxTickLength=10):
        pg.GraphicsWidget.__init__(self)
        self.colorScaleViewBox = pg.ViewBox(enableMenu=False, border=None)

        self.colorScaleViewBox.disableAutoRange(pg.ViewBox.XYAxes)
        self.colorScaleViewBox.setMouseEnabled(x=False, y=False)
        self.colorScaleViewBox.setMinimumWidth(10)
        self.colorScaleViewBox.setMaximumWidth(25)

        self.colorScaleImageItem = pg.ImageItem() # image data will be set in setLut
        self.colorScaleViewBox.addItem(self.colorScaleImageItem)
        self.colorScaleViewBox.setZValue(10)
        self.

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

        logger.debug("lutImg.shape: {}".format(lutImg.shape))
        self.colorScaleImageItem.setImage(lutImg)

        yRange = [0, len(lut)]
        logger.debug("Setting colorScaleViewBox yrange to: {}".format(yRange))

        # Do not set disableAutoRange to True in setRange; it triggers 'one last' auto range.
        # This is why the viewBox' autorange must be False at construction.
        self.colorScaleViewBox.setRange(
            xRange=[0, barWidth], yRange=yRange, padding=0.0,
            update=False, disableAutoRange=False)
