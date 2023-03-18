import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('First name'), sg.InputText()],
            [sg.Text('Last name'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print("ID:",values[1],",",values[0])
    #print('event:', event)
    #print('values: ', values)


window.close()
