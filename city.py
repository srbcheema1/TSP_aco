import math

class City:
	def __init__(self,index,x,y):
		self.index = int(index)
		self.x = int(x)
		self.y = int(y)

	def __repr__(self):
		return str(self)
	
	def __str__(self):
		return "{" + str(self.index) + ": " + str(self.x) + "," + str(self.y) + "}"
	
	def distance(a, b):
		return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
	
	def cost_matrix(cities):
		cost_matrix = []
		rank = len(cities)
		for i in range(rank):
			row = []
			for j in range(rank):
				row.append(City.distance(cities[i], cities[j]))
			cost_matrix.append(row)
		return cost_matrix
	
	def load_cities(file_name):
		cities = []
		with open(file_name) as f:
			index = 1
			for line in f.readlines():
				city = line.split(' ')
				cities.append(City(index,city[0],city[1]))
				index+=1
		return cities