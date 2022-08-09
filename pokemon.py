import os.path

class Pokemon:
    def __init__(self, name):
        path = "pokemon/" + name + ".json"
        if os.path.exists(path):
            file = open()