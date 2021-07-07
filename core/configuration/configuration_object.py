# SINGLETON
class ConfigurationObject:
    __instance = None

    def __init__(self, icon: dict, audio: dict, base: dict):
        if not ConfigurationObject.__instance:
            self.icon_path = icon.get('icon-path')
            self.default_icon = self.icon_path + icon.get('default-icon')

            self.audio_path = audio.get('audio-path')
            self.default_audio = self.audio_path + audio.get('default-audio')

            print(base)
            self.left_arrow = base.get('arrow')[0].get('left-arrow')
            self.right_arrow = base.get('arrow')[0].get('right-arrow')

            self.play_button = base.get('player')[0].get('play-button')
            self.pause_button = base.get('player')[0].get('pause-button')

            self.base_icon = base.get('base-icon')

        else:
            print("Instance already created:", self.getInstance(icon, audio, base))

    def getInstance(cls, icon, audio, base):
        if not cls.__instance:
            cls.__instance = ConfigurationObject(icon, audio, base)
        return cls.__instance
