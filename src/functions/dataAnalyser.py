import pandas as pd

class Analyser:

    @staticmethod
    def analyzer(df:pd.DataFrame,)->dict:
        newdf = Analyser.buildNewDf(df)
        dic = {"count by categorie": Analyser.lenByCategories(newdf),
               "mean len by categorie":Analyser.meanLenByCategories(newdf),
               "the longest by categorie":Analyser.biggests(newdf),
               "the words in capital letters by categorie":Analyser.CpitalWordsByCategories(newdf),
               }
        return dic


    # add new Columns (wcount = word count , len = Number of characters, Capital word = number of Capital word)
    @staticmethod
    def buildNewDf(df:pd.DataFrame,)->pd.DataFrame:
        newdf = df.copy()
        newdf["wcount"] = newdf["Text"].str.count(' ') + 1
        newdf["len"] = newdf["Text"].str.len()
        newdf["Capital word"] = newdf["Text"].apply(Analyser.cuontCapitalWord)

        return newdf

    @staticmethod
    def lenByCategories(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["Biased"].count())
        dic["Not Biased"] = int(df[df["Biased"] == 0]["Biased"].count())
        dic["Unclassified"] = int(df["Biased"].count()) - dic["Biased"] - dic["Not Biased"]

        return dic
    
    @staticmethod
    def CpitalWordsByCategories(df:pd.DataFrame,)->dict:
        dic = dict()
        dic["Biased"] = int(df[df["Biased"]==1]["Capital word"].sum())
        dic["Not Biased"] = int(df[df["Biased"] == 0]["Capital word"].sum())
        dic["all"] = int(df["Capital word"].sum())

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
    
    # Auxiliary function
    @staticmethod
    def isCapitalLetter(let:str)->bool:
        return ord('A') <= ord(let) <= ord('Z')
    
    #Auxiliary function
    @staticmethod
    def isCapitalword(word:str)->bool:
        for let in word:
            if not Analyser.isCapitalLetter(let):
                return False
        return True
    
    @staticmethod
    def cuontCapitalWord(st:str)->int:
        cuont = 0
        # if type(st) == type("a"):
        for word in  st.split(' '):
            if Analyser.isCapitalword(word):
                cuont += 1
        return cuont