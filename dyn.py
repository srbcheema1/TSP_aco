import matplotlib.pyplot as plt

class DynamicPlot():
	def __init__(self):
		plt.ion() # plot interactive mode ON
		self.figure, self.ax = plt.subplots()
		self.cyan_line, = self.ax.plot([],[], 'co-') # emtpy plot
		self.red_line, = self.ax.plot([],[], 'ro') # emtpy plot

	def plot(self, cities, path: list):
		x = []
		y = []

		path.append(path[0])
		for index in range(0, len(path)):
			city = cities[path[index]]
			x.append(city.x)
			y.append(city.y)
		
		self.cyan_line.set_data(x, y)
		self.red_line.set_data([cities[0].x],[cities[0].y])

		self.ax.set_xlim(0, (max(x)+2) * 1.1)
		self.ax.set_ylim(0, (max(y)+2)* 1.1)
		self._flush()

	def _flush(self):
		#We need to draw *and* flush0
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()