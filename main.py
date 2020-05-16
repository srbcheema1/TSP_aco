from aco import ACO, Graph
from dynamic_plot import DynamicPlot
from city import City


def main():
	cities = City.load_cities('./data/data30.txt')
	graph = Graph(cities)
	history,cost = ACO(20, 200, 10, [1.0,3.0], [4.0,2.0], [0.4,0.8]).solve(graph)
	print(cost)
	DynamicPlot().show(cities,history)


if __name__ == '__main__':
	main()