import pandas as pd

class Analyser:



    @staticmethod
    def analyzer(df:pd.DataFrame,)->dict:
        newdf = df.copy()
        newdf["wcount"] = newdf["Text"].str.count(' ')+1
        newdf["len"] = newdf["Text"].str.len()
        dic = {"count by categorie": Analyser.numForCat(newdf),
               "mean len by categorie":Analyser.meanLenByCategories(newdf),
               "the longest by categorie":Analyser.biggests(newdf),
               "the words in capital letters by categorie":{"Biased":None,"not Biased":None,"Unclassified":None},
               }
        return dic


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
        dic["Biased"] = int(df[df["Biased"]==1]["wcount"].mean())
        dic["Not Biased"] = int(df[df["Biased"]==0]["wcount"].mean())
        dic["Null"] = int(df["wcount"].mean())
        # print(newdf.head())

        return dic
    

    def biggests(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = list(df[df["Biased"]==1]["len"].sort_values()[-3:])
        dic["Not Biased"] = list(df[df["Biased"] == 0]["len"].sort_values()[-3:])
        dic["Null"] = list(df["len"].sort_values()[-3:])
        # print(newdf.head())

        return dic

# {'Biased': 860, 'Not Biased': 924, 'Null': 924}
