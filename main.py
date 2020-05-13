import time

from aco import ACO, Graph
from dyn import DynamicPlot
from city import City

def run_file(file_name,plt):
	cities = City.load_cities(file_name)
	graph = Graph(cities)
	history,cost = ACO(10, 100, 1.0, 2.0, 0.6, 10).solve(graph)
	# plt.plot(cities,history[-1])
	for path in history:
		plt.plot(cities,path)
		time.sleep(1)
	print(cost,history[-1])


if __name__ == '__main__':
	plt = DynamicPlot()
	# run_file('./data/srb.txt',plt)
	# time.sleep(3)
	run_file('./data/min.txt',plt)
	time.sleep(3)
	