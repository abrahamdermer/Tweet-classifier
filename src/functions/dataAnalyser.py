import pandas as pd

class Analyser:

    @staticmethod
    def analyzer(df:pd.DataFrame,)->dict:
        newdf = Analyser.buildNewDf(df)
        dic = {"count by categorie": Analyser.lenByCategories(newdf),
               "mean len by categorie":Analyser.meanLenByCategories(newdf),
               "the longest by categorie":Analyser.biggests(newdf),
               "the words in capital letters by categorie":{"Biased":None,"not Biased":None,"all":None},
               }
        return dic


    # add new Columns (wcount = word count , len = Number of characters)
    @staticmethod
    def buildNewDf(df:pd.DataFrame,)->pd.DataFrame:
        newdf = df.copy()
        newdf["wcount"] = newdf["Text"].str.count(' ') + 1
        newdf["len"] = newdf["Text"].str.len()
        return newdf

    @staticmethod
    def lenByCategories(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["Biased"].count())
        dic["Not Biased"] = int(df[df["Biased"] == 0]["Biased"].count())
        dic["Unclassified"] = int(df["Biased"].count()) - dic["Biased"] - dic["Not Biased"]

        return dic
    
    @staticmethod
    def meanLenByCategories(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["wcount"].mean())
        dic["Not Biased"] = int(df[df["Biased"]==0]["wcount"].mean())
        dic["all"] = int(df["wcount"].mean())

        return dic
    
    # the len of 3 tweet longest by categorie
    def biggests(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = list(df[df["Biased"]==1]["len"].sort_values()[-3:])
        dic["Not Biased"] = list(df[df["Biased"] == 0]["len"].sort_values()[-3:])
        dic["all"] = list(df["len"].sort_values()[-3:])

        return dic