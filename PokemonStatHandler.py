import json
class PSH:
    def __init__(self, path):
        self.f = open(path)
        self.data = json.load(file)

    