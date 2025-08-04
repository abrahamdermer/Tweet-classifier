import pandas as pd

class Analyser:

    @staticmethod
    def numForCat(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["Biased"].count())
        dic["Not Biased"] = int(df[df["Biased"] == 0]["Biased"].count())
        dic["Null"] = int(df["Biased"].count()) - dic["Biased"] - dic["Not Biased"]

        return dic
    
    @staticmethod
    def meanLenByCategories(df:pd.DataFrame,)->dict:
        dic = dict()
        newdf = df.copy()
        newdf["WC"] = newdf["Text"].str.count(' ')+1
        dic["Biased"] = int(newdf[newdf["Biased"]==1]["WC"].mean())
        dic["Not Biased"] = int(newdf[newdf["Biased"]==0]["WC"].mean())
        dic["Null"] = int(newdf["WC"].mean())
        # print(newdf.head())

        return dic
    

    def biggests(df:pd.DataFrame,)->dict:
        dic = dict()
        newdf = df.copy()
        newdf["len"] = newdf["Text"].str.len()
        # aa= newdf.sort_values(["Biased","len"]).tail()
        # print(aa["len"])
        dic["Biased"] = list(newdf[newdf["Biased"]==1]["len"].sort_values()[-3:])
        dic["Not Biased"] = list(newdf[newdf["Biased"] == 0]["len"].sort_values()[-3:])
        dic["Null"] = list(newdf["len"].sort_values()[-3:])
        # print(newdf.head())

        return dic

# {'Biased': 860, 'Not Biased': 924, 'Null': 924}
