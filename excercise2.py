# @Author: Hsien-Che Charles Chen
# @Date:   04-22-2017
# @Project: PA2
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 04-26-2017

import plot_square as ps
import numpy as np

# Constants for plotting
# Window Boundaries for plots.
X = [-1, 1]
Y = [-1, 1]
# Vertical points that need to be transformed.
VERTS_3D = [
	[-1, -0.5, 2],
	[1, -0.5, 2],
	[1, 0.5, 2],
	[-1, 0.5, 2]
]

# Caculates matrices for part 1.
def part1(verts_3d):
	k = np.identity(3)
	rt = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0')
	result = equationMul(k, rt, verts_3d)
	display(1, k, rt, result)

# Calculates matrices for part 2.
def part2(verts_3d):
	k = np.identity(3)
	rt = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 2')
	result = equationMul(k, rt, verts_3d)
	display(2, k, rt, result)

# Calculates matrices for part 3.
def part3(verts_3d):
	k = np.identity(3)
	r_x = np.matrix([[1.0, 0, 0], [0, np.sqrt(2)/2, -np.sqrt(2)/2], [0, np.sqrt(2)/2, np.sqrt(2)/2]])
	r_z = np.matrix([[0.5, -np.sqrt(3)/2, 0], [np.sqrt(3)/2, 0.5, 0], [0, 0, 1]])
	r = np.matmul(r_x, r_z)
	t = np.array([0, 0, 2])
	rt = np.hstack((r, np.atleast_2d(t).T))
	result = equationMul(k, rt, verts_3d)
	display(3, k, rt, result)

# Helper function to display part.
def display(part, k, rt, result):
	print "Calculating Part " + str(part) + ": \n"
	print "K = "
	print k
	print ""
	print "[R|t] = "
	print rt
	print ""

	print "Resulting points: "
	for i, vert in enumerate(result):
		print "X_" + str(i) + " = " + str(vert)

	# Inject one more element because plot_square needs it...
	result.append((0,0))

	print "\nPlotting..."
	ps.plot_square(result, X[0], X[1], Y[0], Y[1])

# Helper function to multiply points by the camera equation given
# k and rt matrix settings and vertices.
def equationMul(k, rt, verts_3d):
	result = []
	krt = np.matmul(k, rt)
	for vert in verts_3d:
		mul = np.array([vert[0], vert[1], vert[2], 1])
		vec_homog = np.matmul(krt, mul)
		# Convert result to homogenous
		result.append((vec_homog[0,0]/vec_homog[0,2], vec_homog[0,1]/vec_homog[0,2]))
	return result

# Function to calculate points for excercise 2. Then maps them.
# Call this function to execute file.
def execute_excercise2():
	part1(VERTS_3D)
	part2(VERTS_3D)
	part3(VERTS_3D)

if __name__ == "__main__":
	execute_excercise2()
