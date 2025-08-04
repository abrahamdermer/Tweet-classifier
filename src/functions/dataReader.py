from ..interpase.IdataReader import IdataReader
import pandas as pd


class CreateDataFrame(IdataReader):

    @staticmethod
    def creat_df_from_adrrres(adrres:str) -> pd.DataFrame:
        return pd.read_csv(adrres,sep=r'[,\s]+', engine='python')