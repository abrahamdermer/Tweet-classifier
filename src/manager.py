from .functions.dataReader import CreateDataFrame
from .functions.dataAnalyser import Analyser
from .functions.writer import Writer

class Manager:
    def __init__(self,add):
        self.add = add
        self.data = None
        self.analyzed = None

    def reade(self):
        self.data = CreateDataFrame.creat_df_from_adrrres(self.add)

    def printHead(self):
        print(self.data.head())

    def printTypes(self):
        print(self.data.dtypes)

    def analyse(self):
        self.analyzed = Analyser.analyzer(self.data)

    def tojson(self):
        Writer.writer(self.analyzed)