import PySimpleGUI as sg

font = ('Arial, 15')



info_column = [
    [
        sg.Text('Title', pad=((10, 63), (15, 0))),
        sg.InputText(size=(44, 100), pad=((1, 30), (10, 0))),
    ],
    [
        sg.Text('Description',  pad=((10, 10), (4, 0))),
        sg.InputText(size=(44, 100)),

    ],
    [
        sg.Text('Choose audio', pad=((10, 0), (4, 4))),
        sg.Button(button_text='Browse...', key='__BROWSE_AUDIO__', pad=((0, 93), (4, 4)), enable_events=True),
        sg.Text('default', key='_AUDIO_NAME_'),
        sg.Button(button_text='Play', key='__PLAY_AUDIO__', image_filename='core/ui/static/play-button.png', image_size=(20, 20), pad=((130, 0), (4, 4))),
        sg.Button(button_text='Stop', key='__STOP_AUDIO__', image_filename='core/ui/static/pause-button.png', image_size=(20, 20), pad=((10, 0), (4, 4)))
    ],
    [
        sg.Text('Choose time', pad=((10, 0), (4, 4))),

        sg.Text('sec', pad=((6, 0), (4, 4))),
        sg.Button(key='__DECREASE_SECONDS__', image_filename='core/ui/static/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__SECONDS__'),
        sg.Button(key='__INCREASE_SECONDS__', image_filename='core/ui/static/right-arrow.png', image_size=(20, 20)),

        sg.Text('min', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_MINUTES__', image_filename='core/ui/static/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__MINUTES__'),
        sg.Button(key='__INCREASE_MINUTES__', image_filename='core/ui/static/right-arrow.png', image_size=(20, 20)),

        sg.Text('hour', pad=((40, 0), (4, 4))),
        sg.Button(key='__DECREASE_HOURS__', image_filename='core/ui/static/left-arrow.png', image_size=(20, 20)),
        sg.InputText(size=(2, 100), pad=((1, 1), (10, 10)), key='__HOURS__'),
        sg.Button(key='__INCREASE_HOURS__', image_filename='core/ui/static/right-arrow.png', image_size=(20, 20))
    ]
]

image_column = [
    [
        sg.Image(filename='core/ui/static/icons/plus.png', size=(98, 97), enable_events=True, key='__BROWSE_ICON__'),
    ]
]

layout = [
    [
        sg.Column(layout=image_column, vertical_alignment='left', justification='center', pad=((0, 0), (10, 10))),
        sg.Column(layout=info_column, vertical_alignment='center', justification='center'),
    ],

    # [
    #    sg.Button(button_text='hi',)
    #  ],
    # [sg.Text('File 2'), sg.InputText(), sg.FileBrowse(),
    #  sg.Checkbox('SHA256')
    #  ],
    # [sg.Output(size=(20, 20))],
    # [sg.Submit(), sg.Cancel()]
]

layout_popup = [
    [ ],
    [
        sg.OK(pad=((4, 160), (10, 10))),
    ]
]

def popup_select(elements, is_audio=True):
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

    layout_popup[1].append(sg.Button(button_text='Download', button_color='blue', key=button_download_key, pad=((0, 132), (10, 10))))
    layout_popup[1].append(sg.Cancel(button_color='red'))

    window_popup = sg.Window(window_name, layout=layout_popup, font=font)
    event_popup, values_popup = window_popup.read()
    window_popup.close()
    del window_popup
    if not values_popup[list_box_key]:
        return 'default'
    else:
        return values_popup[list_box_key][0]
