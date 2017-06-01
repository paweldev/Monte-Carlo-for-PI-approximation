import random, sys
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt
import argparse
import numpy as np

drwCircle = None
ax = None

def calculate_pi(point):
	return (point[0]-0.5)**2 + (point[1]-0.5)**2 < 0.25

def main():
	i = 0
	parser = argparse.ArgumentParser();																#tu sie zaczyna parsowanie argumentow command line'a
	group = parser.add_mutually_exclusive_group(required=False)
	group.add_argument("-i", "--iterations_number", nargs="+", help="set the counter manually")

	arguments = parser.parse_args()																	#a tu sie konczy

	plt.axis([-0.5, 0.5, -0.5, 0.5])
	plt.ion()
	plt.gca().set_aspect('equal', adjustable='box')
	drwCircle = plt.Circle((0,0), 0.5, color='r', fill=False)										#tworze kolo
	ax = plt.gca()
	ax.cla()
	ax.set_autoscale_on(False)																		#pozwala recznie ustalic skale
	plt.xticks(np.arange(-0.5,0.6,0.1))																#ustawia skale osi x
	plt.yticks(np.arange(-0.5,0.6,0.1))																#ustawia skale osi y
	ax.add_artist(drwCircle)
	t = ax.text(-0.6, -0.6, "textbar current")														#ustawia polozenie napisu
	count = inside_count = 0

	iterator=0

	if arguments.iterations_number is not None:														#to juz brzydsze byc nie moglo
		stop = int(arguments.iterations_number[0])													#ale python nie wie co to zmienna globalna
		step = 1
	else:																							#zreszta i tak jest lepiej niz bylo
		stop = 1
		step = 0

	while iterator < stop:
			i += 1
			iterator += step
			point = (random.random(), random.random())
			if calculate_pi(point):
				inside_count += 1
				drwDot = plt.Circle((point[0]-0.5, point[1]-0.5), 0.0025, color='g')
			else:
				drwDot = plt.Circle((point[0]-0.5, point[1]-0.5), 0.0025, color='r')
			count += 1
			pi = (inside_count / count) * 4
			ax.add_artist(drwDot)
			t.set_text("Obecna wartość PI: %f" % pi)
			plt.pause(0.0001)

	while True:
		plt.pause(1)

if __name__ == "__main__":
	sys.exit(main())