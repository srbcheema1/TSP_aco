import matplotlib.pyplot as plt

class DynamicPlot():
	def __init__(self):
		plt.ion() # plot interactive mode ON
		self.figure, self.ax = plt.subplots()
		self.ax.plot([],[], 'o') # emtpy plot

	def plot(self, cities, path: list):
		x = []
		y = []
		for city in cities:
			x.append(city.x)
			y.append(city.y)
		self.ax.plot(x, y, 'co')

		path.append(path[0])
		for index in range(1, len(path)):
			i = path[index-1]
			j = path[index]
			self.ax.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='r', length_includes_head=True)

		self.ax.set_xlim(0, (max(x)+2) * 1.1)
		self.ax.set_ylim(0, (max(y)+2)* 1.1)
		self._flush()

	def _flush(self):
		#We need to draw *and* flush0
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()