import time

from aco import ACO, Graph
from dyn import DynamicPlot
from city import City

def run_file(file_name,plt):
	cities = City.load_cities(file_name)
	graph = Graph(cities)
	path,cost = ACO(20, 100, 1.0, 2.0, 0.6, 10).solve(graph)
	plt.plot(cities,path)
	print(cost,path,cities)


if __name__ == '__main__':
	plt = DynamicPlot()
	run_file('./data/min.txt',plt)
	time.sleep(3)