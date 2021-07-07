import PySimpleGUI as sg

from core.configuration.configuration_object import ConfigurationObject

font = ('Arial, 15')

info_column = [
    [
        sg.Text('Title', pad=((10, 63), (15, 0))),
        sg.InputText(size=(44, 100), pad=((1, 30), (10, 0))),
    ],
    [
        sg.Text('Description', pad=((10, 10), (4, 0))),
        sg.InputText(size=(44, 100)),

    ],
    [
        sg.Text('Choose audio', pad=((10, 0), (4, 4))),
        sg.Button(button_text='Browse...', key='__BROWSE_AUDIO__', pad=((0, 93), (4, 4)), enable_events=True),
        sg.Text('default', key='_AUDIO_NAME_'),
        sg.Button(button_text='Play', key='__PLAY_AUDIO__', image_filename='core/ui/static/base/play-button.png',
                  image_size=(20, 20), pad=((130, 0), (4, 4))),
        sg.Button(button_text='Stop', key='__STOP_AUDIO__', image_filename='core/ui/static/base/pause-button.png',
                  image_size=(20, 20), pad=((10, 0), (4, 4)))

    ],
    [
        sg.Text('Choose time', pad=((10, 0), (4, 4))),

        sg.Text('sec', pad=((6, 0), (4, 4))),
        sg.Button(key='__DECREASE_SECONDS__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__SECONDS__', default_text=0, justification='center'),
        sg.Button(key='__INCREASE_SECONDS__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20)),

        sg.Text('min', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_MINUTES__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__MINUTES__', default_text=0, justification='center'),
        sg.Button(key='__INCREASE_MINUTES__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20)),

        sg.Text('hour', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_HOURS__', image_filename='core/ui/static/base/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__HOURS__', default_text=0, justification='center'),
        sg.Button(key='__INCREASE_HOURS__', image_filename='core/ui/static/base/right-arrow.png', image_size=(20, 20))
    ]
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
        sg.Submit(pad=((315, 5), (10, 10))),
        sg.Cancel(pad=((5, 315), (10, 10)))
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
