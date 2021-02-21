import vlc

class AudioPlayer:
    def __init__(self):
        self.vlc_instance = vlc.Instance('--aout=alsa')
        self.player = self.vlc_instance.media_player_new()
        #TODO: add looping
        self.set_volume(100)
        self.current_audio = ""
        self.playing = False

    def set_volume(self, volume):
        vlc.libvlc_audio_set_volume(self.player, volume)

    def play(self, audio_filename):
        if self.current_audio is not audio_filename:
            self.current_audio = audio_filename
            self.audio = self.vlc_instance.media_new(self.current_audio)
            self.player.set_media(self.audio)
            print(f"Starting to play {self.current_audio}")
        self.player.play()
        self.playing = True

    def pause(self):
        if self.playing:
            self.player.pause()
            self.playing = False