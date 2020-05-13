import time

from aco import ACO, Graph
from dyn import DynamicPlot
from city import City

def run_file(file_name,plt):
	cities = City.load_cities(file_name)
	cost_matrix = City.cost_matrix(cities)

	aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
	graph = Graph(cost_matrix, len(cities))
	path, cost = aco.solve(graph)

	plt.plot(cities,path)
	print(cost,path,cities)


if __name__ == '__main__':
	plt = DynamicPlot()
	run_file('./data/min.txt',plt)
	time.sleep(3)