from src.manager import Manager
import pandas as pd

add = "data/tweets_dataset.csv"

manager = Manager(add)
manager.reade()
# manager.printHead()
# manager.printTypes()
print(manager.data["Biased"].isnull().sum())
