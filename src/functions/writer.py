import json

class Writer:

    @staticmethod
    def writerToJson(dic:dict)->None:
        # convert into JSON:
        y = json.dumps(dic)
        with open("results/results.json","w") as f:
            f.write(y)
        print("writed to json")