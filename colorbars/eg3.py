import numpy as np
import pyqtgraph as pg

## Set initial view bounds
win = pg.GraphicsWindow()
view = win.addViewBox()
view.setRange(pg.QtCore.QRectF(0, 0, 600, 600))

# create test pattern background, basically a gradient from left to right
gradCen = 1000  # midpoint of gradient
data = np.zeros([15, 600, 600], dtype=np.uint16)
for i in range(data.shape[1]):
    data[:, i, :] = gradCen - (data.shape[1] / 2) + i
# add horizontal bars, the same color as the extremes of the gradient
data[5:10, :, 200:210] = gradCen - 300
data[5:10, :, 300:310] = gradCen + 300
# add horizontal bars, the color that should be the extremes of the colorscale
data[10:15, :, 200:210] = 0
data[10:15, :, 300:310] = gradCen * 2

# create a color map that goes from full red, to yellow, then to full green
pos = np.array([0.0, 0.5, 1.0])  # absolute scale here relative to the expected data not important I believe
color = np.array([[255, 0, 0, 255], [255, 255, 0, 255], [0, 255, 0, 255]], dtype=np.ubyte)
colmap = pg.ColorMap(pos, color)

# get LUT, first first two params should match the position scale extremes passed to ColorMap().
# I believe last one just has to be >= the difference between the min and max level set later
lut = colmap.getLookupTable(0, 1.0, 2000)

# random image data
img_vals = np.random.normal(size=(100,100))
img = pg.ImageItem(img_vals)
img.setLookupTable(lut)
# img.setLevels([0,2048])   #don't do here, it needs to be after each setImage to work properly

ptime = pg.ptime

updateTime = ptime.time()
fps = 0
i = 0


def updateData():
    global img, data, i, updateTime, fps

    ## Display the data
    img.setImage(data[i])
    # set the levels to the min and max we desire on our scale
    img.setLevels([0, 2000])

    i = (i + 1) % data.shape[0]

    pg.QtCore.QTimer.singleShot(200, updateData)
    now = ptime.time()
    fps2 = 1.0 / (now - updateTime)
    updateTime = now
    fps = fps * 0.9 + fps2 * 0.1

    # print "%0.1f fps" % fps
updateData()


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.instance().exec_()