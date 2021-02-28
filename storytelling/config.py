import json, os

SOUND_DIR = 'sound_directory'
CONFIG_NAME = '/etc/bajkowy/config.json'

class ConfigReader:
    def __init__(self):
        with open(CONFIG_NAME, 'r') as config_file:
            self.config = json.load(config_file)

    def save_config(self):
        with open(CONFIG_NAME, 'w') as config_file:
            print(f"Saving {self.config} to {config_file}")
            json.dump(self.config, config_file)

    def set_sound_directory(self, directory : str):
        self.config[SOUND_DIR] = directory
        self.save_config()

    def get_sound_directory(self) -> str:
        if SOUND_DIR in self.config:
            return self.config[SOUND_DIR]
        return None

    def is_id_valid(self, id : str) -> bool:
        return id.isnumeric()

    def add_song(self, rfid : str, songname : str) -> bool:
        if not self.is_id_valid(rfid):
            return False
        print(f"Saving new configuration: {rfid} - {songname}")
        self.config[rfid] = songname
        self.save_config()
        return True

    def get_song_for_id(self, id : str) -> str:
        print(f"ID{id}:", end=' ')
        if id not in self.config.keys():
            print("failed")
            return None
        songname =  self.config[id]
        print(f"Song: {songname}")
        return songname

    def get_song_for_id_full_path(self, id: str) -> str:
        songname = self.get_song_for_id(id)
        if songname:
            dir = self.get_sound_directory()
            full_path = os.path.join(dir, songname)
            return full_path
        return None