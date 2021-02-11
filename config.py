import json

class ConfigReader:
    def __init__(self, config_filename : str):
        with open(config_filename) as config_file:
            self.config = json.load(config_file)

    def load(self, input : str):
        if input not in self.config.keys():
            return None
        return self.config[input]
