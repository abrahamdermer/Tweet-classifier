from src.manager import Manager
import pandas as pd

address = "data/tweets_dataset.csv"

manager = Manager(address)
manager.reade()
manager.analyse()
manager.writeToJson()