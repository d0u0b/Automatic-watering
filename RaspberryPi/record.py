import pickle
from datetime import datetime
import os
import json
import pytz

class Recoder:
    watering = None
    def __init__(self, record_file):
        self.record_file = record_file
        if os.path.isfile(record_file):
            with open(record_file, "rb") as r:
                self.data = pickle.load(r)
            for data in self.data[::-1]:
                if data["water"]:
                    self.watering = data["time"]
                    break
        else:
            self.data = []

    def chart(self):
        time = []
        temp = []
        humi = []
        sm = []
        for row in self.data:
            time.append(row["time"])
            temp.append(row["temp"])
            humi.append(row["humi"])
            sm.append(row["SM"])
        return json.dumps({
            "time": time,
            "temp": temp,
            "humi": humi,
            "sm": sm
        })

    def get_last(self, num=5):
        return json.dumps(self.data[:-1-num:-1])

    def last_water(self):
        return self.watering

    def record(self, data):
        data["time"] = datetime.now(pytz.timezone("Asia/Taipei")).isoformat()
        if data["water"]:
            self.watering = data["time"]
        self.data.append(data)
        with open(self.record_file, "wb") as w:
            pickle.dump(self.data, w)

    def __str__(self):
        return json.dumps(self.data)