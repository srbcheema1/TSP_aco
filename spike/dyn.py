import matplotlib.pyplot as plt

class DynamicPlot():
  def __init__(self):
    plt.ion() # plot interactive mode ON

    #Set up plot
    self.figure, self.ax = plt.subplots()
    self.ax.plot([],[], 'o') # emtpy plot

    #Autoscale on unknown axis and known lims on the other
    self.ax.autoscale(True,axis='y')
    self.ax.set_xlim(0, 10)

  def plot(self, xdata, ydata):
    self.ax.plot(xdata,ydata,'co')
    #We need to draw *and* flush0
    self.figure.canvas.draw()
    self.figure.canvas.flush_events()
        

if __name__ == "__main__":
  d = DynamicPlot()
  import numpy as np
  import time
  xdata = []
  ydata = []
  for x in np.arange(0,10,0.5):
      xdata.append(x)
      ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
      d.plot(xdata, ydata)
      time.sleep(1)