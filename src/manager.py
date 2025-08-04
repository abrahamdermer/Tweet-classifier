from .functions.dataReader import CreateDataFrame
from .functions.dataAnalyser import Analyser

class Manager:
    def __init__(self,add):
        self.add = add
        self.data = None

    def reade(self):
        self.data = CreateDataFrame.creat_df_from_adrrres(self.add)

    def printHead(self):
        print(self.data.head())

    def printTypes(self):
        print(self.data.dtypes)

    def cuntBycat(self):
        print(Analyser.numForCat(self.data))

    def meanBycat(self):
        print(Analyser.meanLenByCategories(self.data))

    def big(self):
        print(Analyser.biggests(self.data))
