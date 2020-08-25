from numpy import linspace, meshgrid, array, sin, cos, pi, abs
from scipy.special import sph_harm
from mayavi import mlab

theta_1d = linspace(0, pi, 91)
phi_1d = linspace(0, 2 * pi, 181)

theta_2d, phi_2d = meshgrid(theta_1d, phi_1d)
xyz_2d = array([sin(theta_2d) * sin(phi_2d),
                sin(theta_2d) * cos(phi_2d),
                cos(theta_2d)])
l = 3
m = 0

Y_lm = sph_harm(m, l, phi_2d, theta_2d)
r = abs(Y_lm.real) * xyz_2d

mlab.figure(size=(700, 830))
mlab.mesh(r[0], r[1], r[2], scalars=Y_lm.real, colormap="cool")
mlab.view(azimuth=0, elevation=75, distance=2.4, roll=-50)
mlab.savefig("Y_%i_%i.jpg" % (l, m))
mlab.show()