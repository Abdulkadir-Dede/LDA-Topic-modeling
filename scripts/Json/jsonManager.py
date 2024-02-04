
import json


class JsonManager:

    def ReadJson(filename):
        with open(filename,"r", encoding="utf-8") as f:
            return json.loads(f.read()) 