import matplotlib.pyplot as plt
import seaborn as sns

from deepspace.DataSpace import DataSpace
from deepspace.transformers.Transformer import Transformer
from deepspace.transformers.exploration.plot.Abstract import AbstractPlot

class ScatterPlot(AbstractPlot):
    def __init__(self, x, y, xlabel=None, ylabel=None, figsize=(7, 7), color='red', hue=None):
        AbstractPlot.__init__(self, x, y, xlabel=xlabel, ylabel=ylabel, figsize=figsize, color=color, hue=hue)
    def transform(self, ds:DataSpace):
        self.ds = ds
        self.plot(self.x, self.y, color=self.color, hue=self.hue)
        return ds
    def plot(self, x, y, color='red', hue=None):
        self.separator(n=1, caller=self, string=f'plot for {x}/{y}')

        plt.figure(figsize=self.figsize)
        sns.scatterplot(x=self.ds.data[x], y=self.ds.data[y],  color=color, hue=hue)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
