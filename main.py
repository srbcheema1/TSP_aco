import time

from aco import ACO, Graph
from dyn import DynamicPlot
from city import City

def run_file(file_name,plt):
	cities = City.load_cities(file_name)
	graph = Graph(cities)
	history,cost = ACO(20, 100, 10, [1.0,3.0], [4.0,2.0], [0.4,0.8]).solve(graph)

	print(cost,history[-1])
	for path in history:
		plt.plot(cities,path)
		time.sleep(1)


if __name__ == '__main__':
	plt = DynamicPlot()
	run_file('./data/data1.txt',plt)
	time.sleep(3)
	