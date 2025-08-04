import pandas as pd

class Analyser:

    @staticmethod
    def numForCat(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["Biased"].count())
        dic["Not Biased"] = int(df[df["Biased"] == 0]["Biased"].count())
        dic["Null"] = int(df["Biased"].count()) - dic["Biased"] - dic["Not Biased"]

        return dic
     
