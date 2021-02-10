import vlc

class AudioPlayer:
    def __init__(self):
        self.instance = vlc.Instance('--aout=alsa')
        self.player = self.instance.media_player_new()
        self.set_volume(90)
        self.current_audio = ""

    def set_volume(self, volume):
        vlc.libvlc_audio_set_volume(self.player, volume)

    def play(self, audio_filename):
        if self.current_audio is not audio_filename:
            self.current_audio = audio_filename
            self.audio = self.instance.media_new(self.current_audio)
            self.player.set_media(self.audio)
        self.player.play()

    def pause(self):
        self.player.pause()