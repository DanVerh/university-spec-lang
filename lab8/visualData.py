import pandas
from matplotlib import pyplot


class VisualData:
    def __init__(self):
        self.data = pandas.read_csv('./inputs/data.csv')

    def getExtremes(self):
        extremes = self.data.max()
        return extremes

    def printExtremes(self):
        print(self.getExtremes())

    def simpleVisual(self):
        pyplot.figure(figsize=(10, 5))
        pyplot.plot(self.data['Column1'], label='Column1')
        pyplot.title('Simple Visualization')
        pyplot.xlabel('Index')
        pyplot.ylabel('Value')
        pyplot.legend()
        pyplot.savefig('./outputs/simpleVisual.png')
        pyplot.show()

    def multDiagrams(self):
        fig, axes = pyplot.subplots(nrows=1, ncols=2, figsize=(12, 5))
        axes[0].scatter(self.data['Column3'], self.data['Column4'], label='Column3 vs Column4', color='green')
        axes[0].set_title('Scatter Plot')
        axes[1].hist(self.data['Column5'], bins=20, label='Column5', color='green', alpha=0.7)
        axes[1].set_title('Histogram')
        pyplot.tight_layout()
        pyplot.show()