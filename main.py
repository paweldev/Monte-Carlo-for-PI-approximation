import random, sys
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt
import argparse

drwCircle = None
ax = None
radius = 1.2

def calculate_pi(point):
	return point[0]**2 + point[1]**2 < radius**2

def draw():
	i += 1
	point = (random.random(), random.random())
	if calculate_pi(point):
		inside_count += 1
	count += 1
	pi = (inside_count / count) * 4
	drwDot = plt.Circle((point[0]-0.5, point[1]-0.5), 0.005, color='g')
	ax.add_artist(drwDot)
	if i % 15 == 0:
		t.set_text("Obecna wartość PI: %f" % pi)
		plt.pause(0.0001)

def main():
	i = 0
	parser = argparse.ArgumentParser();
	group = parser.add_mutually_exclusive_group(required=False)
	group.add_argument("-i", "--iterations_number", nargs="+", help="set the counter manually")

	arguments = parser.parse_args()

	plt.axis([0,1,0,1])
	plt.xlim(-0.75, 0.75)
	plt.ylim(-0.75, 0.75)
	plt.gca().set_aspect('equal', adjustable='box')
	drwCircle = plt.Circle((0,0), 0.5, color='r', fill=False)
	ax = plt.gca()
	ax.cla()
	ax.add_artist(drwCircle)
	t = ax.text(-1.2, -0.9, "textbar current")
	#ax.add_artist(t)
	count = inside_count = 0

	if arguments.iterations_number is not None:
		j = int(arguments.iterations_number[0])
		for x in range(1,j):
			i += 1
			point = (random.random(), random.random())
			if calculate_pi(point):
				inside_count += 1
			count += 1
			pi = (inside_count / count) * 4
			drwDot = plt.Circle((point[0]-0.5, point[1]-0.5), 0.005, color='g')
			ax.add_artist(drwDot)
			#if i % 5 == 0:
			t.set_text("Obecna wartość PI: %f" % pi)
			plt.pause(0.001)
	else:
		while True:
			i += 1
			point = (random.random(), random.random())
			if calculate_pi(point):
				inside_count += 1
			count += 1
			pi = (inside_count / count) * 4
			drwDot = plt.Circle((point[0]-0.5, point[1]-0.5), 0.005, color='g')
			ax.add_artist(drwDot)
			if i % 15 == 0:
				t.set_text("Obecna wartość PI: %f" % pi)
				plt.pause(0.0001)

if __name__ == "__main__":
	sys.exit(main())