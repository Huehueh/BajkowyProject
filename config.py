import json

class ConfigReader:
    def __init__(self, config_filename : str):
        with open(config_filename) as config_file:
            self.config = json.load(config_file)

    def load(self, input : str) -> str:
        print(f"Loading id {input}", end=' ')
        print("Keys", self.config.keys())
        if input not in self.config.keys():
            print("failed")
            return None
        songname =  self.config[input]
        print(songname)
        return songname
