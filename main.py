import time

from notifypy import Notify
import simpleaudio as sa
from core.finders.local_audio_finder import LocalAudioFinder
from core.timer import Timer
import threading
import PySimpleGUI as sg
from pygame import mixer

from core.ui.user_interface import layout, font, popup_select

if __name__ == '__main__':
    sg.theme('Dark')
    mixer.init()
    window = sg.Window("LetMeKnow", layout, font=font)
    while True:
        event, values = window.read()
        print(event, values)  # debug
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == '__BROWSE_AUDIO__':
            local_audio_finder = LocalAudioFinder.getInstance()
            files = local_audio_finder.find_all()
            audio_name = popup_select(local_audio_finder.audio_list)
            window['_AUDIO_NAME_'].update(audio_name)
        if event == '__PLAY_AUDIO__':
            # TODO add multithreading
            local_audio_finder = LocalAudioFinder.getInstance()
            audio_name = window['_AUDIO_NAME_'].get() + '.mp3'
            mixer.music.load(audio_name)
            mixer.music.play()
        if event == '__STOP_AUDIO__':
            mixer.music.stop()
        if event == '__BROWSE_ICON__':
            pass






    # input_value = int(input())
    # timer = Timer(input_value)
    # notify = Notify()
    # notify.title = "Cool Title"
    # notify.message = "Even cooler message."
    # time.sleep(timer.finish_time)
    # notify.send()


