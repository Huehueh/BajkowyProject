import json, os

SOUND_DIR = "sound_directory"

class ConfigReader:
    def __init__(self, config_filename : str):
        self.config_filename = config_filename
        with open(self.config_filename, 'r') as config_file:
            self.config = json.load(config_file)

    def save_config(self):
        with open(self.config_filename, 'w') as config_file:
            json.dump(self.config, config_file)

    def set_sound_directory(self, directory : str):
        self.config[SOUND_DIR] = directory
        self.save_config()

    def get_sound_directory(self) -> str:
        if SOUND_DIR in self.config:
            return self.config[SOUND_DIR]
        return None

    def add_song(self, id : str, songname : str):
        self.config[id] = songname
        self.save_config()

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