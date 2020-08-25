# -*- coding: utf-8 -*-
"""
Simple examples demonstrating the use of GLMeshItem.

"""

## Add path to library (just for examples; you do not need this)


from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)

import numpy as np


## Example 1:
## Array of vertex positions and array of vertex indexes defining faces
## Colors are specified per-face

verts = np.array([
    [0, 0, 0],  # 0
    [2, 0, 0],  # 1
    [2, 5, 0],  # 2
    [0, 5, 0],  # 3
    [0, 0, 1],  # 4
    [2, 0, 1],  # 5
    [2, 5, 1],  # 6
    [0, 5, 1],  # 7
])
faces = np.array([
    # bottom face
    [0, 1, 2],
    [2, 3, 0],
    # top face
    [4, 5, 6],
    [6, 7, 4],
    # back face
    [0, 1, 5],
    [0, 4, 5],
    # front face
    [2, 3, 7],
    [2, 6, 7],
    # right face
    [1, 2, 6],
    [1, 5, 6],
    # left face
    [0, 3, 7],
    [0, 4, 7],
])
colors = np.array([
    [1, 0, 0, 0.8],
    [1, 0, 0, 0.8],
    [1, 1, 0, 0.8],
    [1, 1, 0, 0.8],
    [1, 0, 0, 0.8],
    [1, 0, 0, 0.8],
    [1, 1, 0, 0.8],
    [1, 1, 0, 0.8],
    [1, 0, 0, 0.8],
    [1, 0, 0, 0.8],
    [1, 1, 0, 0.8],
    [1, 1, 0, 0.8]
])

## Mesh item will automatically compute face normals.
m1 = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors, smooth=False)
m1.translate(5, 5, 0)
m1.setGLOptions('additive')
w.addItem(m1)

#
# ## Example 2:
# ## Array of vertex positions, three per face
# verts = np.empty((36, 3, 3), dtype=np.float32)
# theta = np.linspace(0, 2*np.pi, 37)[:-1]
# verts[:,0] = np.vstack([2*np.cos(theta), 2*np.sin(theta), [0]*36]).T
# verts[:,1] = np.vstack([4*np.cos(theta+0.2), 4*np.sin(theta+0.2), [-1]*36]).T
# verts[:,2] = np.vstack([4*np.cos(theta-0.2), 4*np.sin(theta-0.2), [1]*36]).T
#
# ## Colors are specified per-vertex
# colors = np.random.random(size=(verts.shape[0], 3, 4))
# m2 = gl.GLMeshItem(vertexes=verts, vertexColors=colors, smooth=False, shader='balloon',
#                    drawEdges=True, edgeColor=(1, 1, 0, 1))
# m2.translate(-5, 5, 0)
# w.addItem(m2)




    


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
