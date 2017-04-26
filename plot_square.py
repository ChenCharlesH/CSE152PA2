# @Author: Hsien-Che Charles Chen
# @Date:   04-25-2017
# @Project: plot_square
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 04-25-2017

import numpy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def plot_square(verts, x_min, x_max, y_min, y_max):
	codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
	path = Path(verts, codes)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	patch = patches.PathPatch(path, facecolor='none', lw=2)
	ax.add_patch(patch)
	ax.set_xlim(x_min, x_max)
	ax.set_ylim(y_min, y_max)
	plt.show()
