import random

class Graph(object):
	def __init__(self, cost_matrix: list, size: int):
		self.cost = cost_matrix
		self.size = size
		self.pheromone = [[1 / (size * size) for j in range(size)] for i in range(size)]



class ACO(object):
	def __init__(self, ant_count: int, generations: int, alpha: float, beta: float, rho: float, q: int):
		self.Q = q #pheromone intensity
		self.rho = rho #pheromone residual coefficient
		self.beta = beta #relative importance of heuristic information
		self.alpha = alpha #relative importance of pheromone
		self.ant_count = ant_count
		self.generations = generations


	def _update_pheromone(self, graph: Graph, ants: list):
		for i, row in enumerate(graph.pheromone):
			for j, col in enumerate(row):
				graph.pheromone[i][j] *= self.rho
				for ant in ants:
					graph.pheromone[i][j] += ant.pheromone_delta[i][j]


	def solve(self, graph: Graph):
		best_cost = float('inf')
		best_solution = []
		for gen in range(self.generations):
			ants = [_Ant(self, graph) for i in range(self.ant_count)]
			for ant in ants:
				cost = ant.travel()
				if cost < best_cost:
					best_cost = cost
					best_solution = [] + ant.path
			self._update_pheromone(graph, ants)
			# print('generation #{}, best cost: {}, path: {}'.format(gen, best_cost, best_solution))
		return best_solution, best_cost



class _Ant(object):
	def __init__(self, aco: ACO, graph: Graph):
		self.aco = aco
		self.graph = graph

		self.pheromone_delta = []  # the local increase of pheromone
		self.allowed = {i for i in range(graph.size)}  # nodes which are allowed for the next selection
		self.eta = [[0 if i == j else 1 / graph.cost[i][j] for j in range(graph.size)] for i in range(graph.size)]  # heuristic information

		self.path = []  # path list
		self.curr = random.randint(0, graph.size - 1)  # start from any node
		self.path.append(self.curr)
		self.allowed.remove(self.curr)


	def travel(self):
		for i in range(self.graph.size - 1):
			self._select_next()
		self._update_pheromone_delta()
		return self._travel_cost()


	def _travel_cost(self):
		cost = 0
		for index in range(1, len(self.path)):
			i = self.path[index-1]
			j = self.path[index]
			cost += self.graph.cost[i][j]
		cost += self.graph.cost[self.path[0]][self.path[-1]] #round trip
		return cost


	def _select_next(self):
		denominator = 0
		for i in self.allowed:
			denominator += self.graph.pheromone[self.curr][i]**self.aco.alpha * self.eta[self.curr][i]**self.aco.beta

		probabilities = [0 for i in range(self.graph.size)]  # probabilities for moving to a node in the next step
		for i in self.allowed:
			probabilities[i] = self.graph.pheromone[self.curr][i]**self.aco.alpha * self.eta[self.curr][i]**self.aco.beta / denominator

		self.curr = self._select_according_to_probability(probabilities)
		self.allowed.remove(self.curr)
		self.path.append(self.curr)


	def _select_according_to_probability(self,probabilities):
		rand = random.random()
		for i, probability in enumerate(probabilities):
			rand -= probability
			if rand <= 0:
				return i


	def _update_pheromone_delta(self):
		self.pheromone_delta = [[0 for j in range(self.graph.size)] for i in range(self.graph.size)]
		for _ in range(1, len(self.path)):
			i = self.path[_ - 1]
			j = self.path[_]
			self.pheromone_delta[i][j] = self.aco.Q