from src.manager import Manager
import pandas as pd

add = "data/tweets_dataset.csv"

manager = Manager(add)
manager.reade()
manager.printer()
# print(pd.read_csv(add))