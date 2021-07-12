
import sys
import re
from core.configuration.parser import Parser, Serializer
from core.exceptions.validation_exceptions import *
from core.finders.local_audio_finder import LocalAudioFinder
from core.finders.local_icon_finder import LocalIconFinder
import PySimpleGUI as sg
from pygame import mixer

from core.timer import Timer
from core.ui.user_interface import layout, font, popup_select, change_value, set_default, get_data_from_window, \
    update_notify_list
from core.validator import Validator


def configure():
    try:
        if len(sys.argv) != 2:
            sys.exit(0)
        file = open(sys.argv[1])
        config_data = Parser.parse(file=file)
        config_object = Serializer.serialize(config_data=config_data)
        return config_object

    except FileNotFoundError as e:
        print(e)
        sys.exit(0)


#TODO add list of notify
if __name__ == '__main__':
    sg.theme('Dark')

    config_object = configure()
    local_audio_finder = LocalAudioFinder.getInstance()
    local_icon_finder = LocalIconFinder.getInstance()
    mixer.init()
    window = sg.Window("LetMeKnow", layout, font=font)
    while True:
        event, values = window.read()
        print(event, values)  # debug
        if event in (None, 'Exit', 'Cancel'):
            break

        if event == '__BROWSE_AUDIO__':
            local_audio_finder = LocalAudioFinder.getInstance()
            local_audio_finder.find_all(config_object.audio_path)
            audio_name = popup_select(local_audio_finder.audio_list)
            window['_AUDIO_NAME_'].update(audio_name)

        if event == '__PLAY_AUDIO__':
            local_audio_finder = LocalAudioFinder.getInstance()
            audio_name = local_audio_finder.find_by_name(window['_AUDIO_NAME_'].get(), config_object.audio_path)
            mixer.music.load(audio_name)
            mixer.music.play()

        if event == '__STOP_AUDIO__':
            mixer.music.stop()

        if event == '__BROWSE_ICON__':
            local_icon_finder.find_all(config_object.icon_path)
            image_name = popup_select(local_icon_finder.format_names(), is_audio=False)
            window['__BROWSE_ICON__'].update(local_icon_finder.find_by_name(image_name, config_object.icon_path))
            window['__BROWSE_ICON__'].Filename = local_icon_finder.find_by_name(image_name, config_object.icon_path)
            window['__BROWSE_ICON__'].set_size((120, 139))

        if re.match(r'__INCREASE__*', event) or re.match(r'__DECREASE__*', event):
            event = event.split('__')[1].split('_')
            type_time = event[1]
            type_event = True if event[0] == 'INCREASE' else False
            change_value(type_time, window, is_increase=type_event)

        if event == '__CLEAR__':
            event = sg.popup_ok_cancel('Do you want to clear all data? All of unsaved information will be reset', font=font)
            if event == 'OK':
                set_default(window, config_object)

        if event == '__SUBMIT__':
            data = get_data_from_window(window, config_object)
            validator = Validator()
            print(data)
            try:
                validator.validate(data, config_object)
            except TitleValidationException as e:
                sg.popup_ok(e.txt)
                set_default(window, config_object, 'title')
                continue
            except DescriptionValidationException as e:
                sg.popup_ok(e.txt)
                set_default(window, config_object, 'desc')
                continue
            except IconValidationException as e:
                sg.popup_ok(e.txt)
                set_default(window, config_object, 'icon')
                continue
            except TimeValidationException as e:
                sg.popup_ok(e.txt)
                set_default(window, config_object, 'time')
                continue
            timer = Timer(data)
            timer.start()
            update_notify_list(window, timer.notify, data)



    # input_value = int(input())
    # timer = Timer(input_value)
    # notify = Notify()
    # notify.title = "Cool Title"
    # notify.message = "Even cooler message."
    # time.sleep(timer.finish_time)
    # notify.send()


