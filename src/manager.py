from .functions.dataReader import CreateDataFrame

class Manager:
    def __init__(self,add):
        self.add = add
        self.data = None

    def reade(self):
        self.data = CreateDataFrame.creat_df_from_adrrres(self.add)

    def printer(self):
        print(self.data.head())