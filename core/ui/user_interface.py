import PySimpleGUI as sg

font = ('Arial, 15')

# choose_audio_scrolling_text = [
#     ]
#         sg.InputText(size=(44, 100))
#     ]
# ]



icon_column = [
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
        sg.Button(button_text='Browse...', pad=((0, 93), (4, 4)), enable_events=True),
        sg.Text('default', key='_AUDIO_NAME_'),
        sg.Button(button_text='Play', image_filename='core/ui/static/play-button.png', image_size=(20, 20), pad=((130, 0), (4, 4))),
        sg.Button(button_text='Stop', image_filename='core/ui/static/pause-button.png', image_size=(20, 20), pad=((10, 0), (4, 4)))
    ]
]

image_column = [
    [
        sg.Image(filename='core/ui/static/plus.png', size=(80, 80)),
    ]
]

layout = [
    [
        # sg.Column(layout=icon_column, vertical_alignment='center', justification='center')
        sg.Column(layout=image_column, vertical_alignment='left', justification='center', pad=((0, 0), (10, 10))),
        sg.Column(layout=icon_column, vertical_alignment='center', justification='center'),
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

# TODO fix bug
def popup_select(elements):
    layout_popup = [
        [
            sg.Listbox(elements, key='_AUDIO_', size=(45, len(elements)), highlight_background_color='green',
                       highlight_text_color='white', select_mode='extended', bind_return_key=True),
        ],
        [
            sg.OK(pad=((4, 215), (10, 10))),
            sg.Cancel(button_color='red')
        ]
    ]
    window_popup = sg.Window('Choose audio name', layout=layout_popup)
    event_popup, values_popup = window_popup.read()
    window_popup.close()
    del window_popup
    if not values_popup['_AUDIO_']:
        return 'default'
    else:
        return values_popup['_AUDIO_'][0]
