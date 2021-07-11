import PySimpleGUI as sg


from core.finders.local_audio_finder import LocalAudioFinder

font = ('Arial, 15')

info_column = [
    [
        sg.Text('Title', pad=((10, 63), (15, 0))),
        sg.InputText(size=(44, 100), pad=((1, 30), (10, 0)), enable_events=True, key='__TITLE__'),
    ],
    [
        sg.Text('Description', pad=((10, 10), (4, 0))),
        sg.InputText(size=(44, 100), enable_events=True, key='__DESC__'),

    ],
    [
        sg.Text('Choose audio', pad=((10, 0), (4, 4))),
        sg.Button(button_text='Browse...', key='__BROWSE_AUDIO__', pad=((0, 93), (4, 4)), enable_events=True),
        sg.Text('Dope', key='_AUDIO_NAME_'),
        sg.Button(button_text='Play', key='__PLAY_AUDIO__', image_filename='core/ui/static/base/play-button.png',
                  image_size=(20, 20), pad=((130, 0), (4, 4))),
        sg.Button(button_text='Stop', key='__STOP_AUDIO__', image_filename='core/ui/static/base/pause-button.png',
                  image_size=(20, 20), pad=((10, 0), (4, 4)))

    ],
    [
        sg.Text('Choose time', pad=((10, 0), (4, 4))),

        sg.Text('sec', pad=((6, 0), (4, 4))),
        sg.Button(key='__DECREASE_SECONDS__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__SECONDS__', default_text=0, justification='center', disabled=True),
        sg.Button(key='__INCREASE_SECONDS__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20)),

        sg.Text('min', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_MINUTES__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__MINUTES__', default_text=0, justification='center', disabled=True),
        sg.Button(key='__INCREASE_MINUTES__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20)),

        sg.Text('hour', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_HOURS__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__HOURS__', default_text=0, justification='center', disabled=True),
        sg.Button(key='__INCREASE_HOURS__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20))
    ],
]

image_column = [
    [
        sg.Image(filename='core/ui/static/base/plus.png', size=(120, 139), enable_events=True, key='__BROWSE_ICON__', background_color='white'),
    ]
]

layout = [
    [
        sg.Column(layout=image_column, vertical_alignment='left', justification='center', pad=((0, 0), (10, 10))),
        sg.Column(layout=info_column, vertical_alignment='center', justification='center'),
    ],
    [
            sg.Listbox(values=[], key='__LIST__', size=(70, 10), pad=((3, 3),(2, 2)))
    ],
    [
            sg.Submit(pad=((600, 10), (10, 10)), key='__SUBMIT__', button_color='green'),
            sg.Button('Clear', pad=((0, 0), (10, 11)), key='__CLEAR__', button_color='red')
    ]

]


# def configure_layouts(config_object: ConfigurationObject, window: sg.Window):
#     window['__PLAY_AUDIO__'].update(
#         sg.Button(button_text='Play', key='__PLAY_AUDIO__', image_filename='core/ui/static/play-button.png',
#                   image_size=(20, 20), pad=((130, 0), (4, 4)))
#     )
#
#     info_column[2].append(
#         sg.Button(button_text='Stop', key='__STOP_AUDIO__', image_filename='core/ui/static/pause-button.png',
#                   image_size=(20, 20), pad=((10, 0), (4, 4))))
#
#     string_patterns = [
#         [
#             'sec', 'SECONDS'
#         ],
#         [
#             'min', 'MINUTES'
#         ],
#         [
#             'hour', 'HOURS'
#         ]
#     ]
#     for i in range(3):
#         text, key = string_patterns[0][0], string_patterns[0][1]
#         info_column[3].append(sg.Text(text, pad=((6, 0), (4, 4))))
#         info_column[3].append(sg.Button(key='__DECREASE_{}__'.format(key), image_filename=config_object.left_arrow, image_size=(20, 20)))
#         info_column[3].append(sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__{}__'.format(key)))
#         info_column[3].append(sg.Button(key='__INCREASE_{}__'.format(key), image_filename='', image_size=(20, 20)),)

def popup_select(elements, is_audio=True):
    layout_popup = [
        [],
        [
            sg.OK(pad=((4, 160), (10, 10))),
        ]
    ]

    list_box_key = '_{}_'
    button_download_key = '__DOWNLOAD_{}__'
    window_name = 'Choose {}'

    if is_audio:
        list_box_key = list_box_key.format('AUDIO')
        button_download_key = button_download_key.format('AUDIO')
        window_name.format('audio')
    else:
        list_box_key = list_box_key.format('ICON')
        button_download_key = button_download_key.format('ICON')
        window_name.format('icon')

    layout_popup[0].append(
        sg.Listbox(
            elements, key=list_box_key, size=(45, len(elements)), highlight_background_color='green',
            highlight_text_color='white', select_mode='extended', bind_return_key=True
        )
    )

    layout_popup[1].append(
        sg.Button(button_text='Download', button_color='blue', key=button_download_key, pad=((0, 132), (10, 10))))
    layout_popup[1].append(sg.Cancel(button_color='red'))
    window_popup = sg.Window(window_name, layout=layout_popup, font=font)
    event_popup, values_popup = window_popup.read()
    window_popup.close()
    del window_popup
    if not values_popup[list_box_key]:
        return 'default'
    else:
        return values_popup[list_box_key][0]


def change_value(type_time, window, is_increase=True):
    key = '__{}__'.format(type_time)
    value = int(window[key].get())
    if is_increase:
        if value == 60 and type_time != '__HOURS__':
            return
        value += 1
    else:
        if value == 0:
            return
        value -= 1
    window[key].update(value)


def set_default(window, config_object, field=None):
    short_keys = {
        'title': ['__TITLE__', ''],
        'desc': ['__DESC__', ''],
        'icon': ['__BROWSE_ICON__', config_object.base_icon, (120, 139)],
        'audio': ['_AUDIO_NAME_', 'Dope'],
        'time': [
            ['__SECONDS__', 0],
            ['__MINUTES__', 0],
            ['__HOURS__', 0]
        ]
    }

    if field is None:
        for (k, v) in short_keys.items():
            if k == 'time':
                for t in v:
                    window[t[0]].update(t[1])
                continue
            window[v[0]].update(v[1])
            if k == 'icon':
                window[v[0]].set_size(size=(120, 139))

        # window['__TITLE__'].update('')
        # window['__DESC__'].update('')
        # window['__BROWSE_ICON__'].update(config_object.base_icon)
        # window['__BROWSE_ICON__'].set_size(size=(120, 139))
        # window['_AUDIO_NAME_'].update('Dope')
        # window['__SECONDS__'].update(0)
        # window['__MINUTES__'].update(0)
        # window['__HOURS__'].update(0)
    else:
        if field == 'time':
            for t in short_keys[field]:
                window[t[0]].update(t[1])
            return
        k, v = short_keys[field][0], short_keys[field][1]
        window[k].update(v)
        if field == 'icon':
            window[k].set_size(size=(120, 139))

def get_data_from_window(window: sg.Window, config_object):
    local_audio_finder = LocalAudioFinder()
    result = {
        'title': window['__TITLE__'].get(),
        'description': window['__DESC__'].get(),
        'icon': window['__BROWSE_ICON__'].Filename,
        'audio': local_audio_finder.find_by_name(window['_AUDIO_NAME_'].get(), config_object.audio_path),
        'time': int(window['__SECONDS__'].get()) + int(window['__MINUTES__'].get()) * 60 + int(window['__HOURS__'].get()) * 3600}
    return result







