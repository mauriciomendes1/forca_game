import PySimpleGUI as sg
from back import *


#PEQUENO JOGO DA FORCA
#DESENVOLVIDO POR MAURÍCIO MENDES

sg.theme('LightBlue2')


def inicial():
    palavra, dica = sortear_tema()
    canvas = sg.Canvas(size=(300, 150),background_color='azure', key='-CANVAS-')
    tentativas = 7

    layout = [
        [sg.Text('Dica:', size=(4, 1)), sg.Text('', size=(20, 1), key='-DICA-')],
        [[canvas]],
        [sg.Text('', key='-LETRAS-', size=(len(palavra) + 1, 1), relief=sg.RELIEF_GROOVE, font=('Arial Black', 20))],
        [sg.Text('Letra'), sg.InputText('', size=(2, 1), key='-PALPITE-'), sg.Button('Enviar', key='-SENT-', bind_return_key='Enter')]
    ]

    window = sg.Window('FORCA', layout, element_justification='center', size=(400, 300), finalize=True)
    tkc = canvas.TKCanvas
    window['-LETRAS-'].update(len(palavra) * '*')
    window['-DICA-'].update(dica.upper())
    #desenhando boneco


    tkc.create_line(240, 20, 240, 120, fill='black')
    tkc.create_line(240, 120, 210, 130)
    tkc.create_line(240, 120, 270, 130)

    tkc.create_line(240, 20, 190, 20, fill='black')
    tkc.create_line(190, 20, 190, 40)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        
        if tentativas > 1:
            if event == '-SENT-':
                if len(values['-PALPITE-']) > 1 or len(values['-PALPITE-']) < 1:
                    sg.popup_ok('Informe uma letra por palpite!')
                
                if values['-PALPITE-'].isnumeric():
                    sg.popup_ok('Informe apenas letras!')
                
                if formando_palavra(values['-PALPITE-'], palavra) == palavra:
                    sg.popup('''PARABÉNS, VC ACERTOU!!!
                            A palavra é ''' + palavra.upper())

                    break
                
                window['-LETRAS-'].update(formando_palavra(values['-PALPITE-'].upper(), palavra.upper()))
                if not consultar_letra(values['-PALPITE-'], palavra):
                    tentativas -= 1
                
                if tentativas == 6:
                    tkc.create_oval(180,40, 200, 60, outline='black') #cabeça do boneco
                elif tentativas == 5:
                    tkc.create_line(190, 60, 190, 100, fill='black') #corpo do boneco
                elif tentativas == 4:
                    tkc.create_line(190, 65, 175, 80, fill='black') #braço esquerdo
                elif tentativas == 3:
                    tkc.create_line(190, 65, 205, 80, fill='black') #braço direito
                elif tentativas == 2:
                    tkc.create_line(190, 100, 175, 115,fill='black') #perna esquerda
                elif tentativas == 1:
                    tkc.create_line(190, 100, 205, 115, fill='black') #perna direita
                
        else:
            sg.popup_ok('''Tentativas esgotadas!
                            A palavra é ''' + palavra.upper())
            break

            
        
inicial()