# CODIGO DESENVOLVIDO POR DANIEL COSTA CARVALHO MARTINS

# IMPORTA O PYSIMPLEGUI.
import PySimpleGUI as sg

# CRIA O LAYOUT DA JANELA 1.
def calcwin():
    sg.theme('NeonYellow1')
    layout = [
        [sg.Text('Calculadora de IMC (Indice de massa corporal)')],
        [sg.Text('Digite seu peso no primeiro campo e sua altura no segundo')],
        [sg.InputText(key = 'weight')],
        [sg.InputText(key = 'height')],
        [sg.Button('Calcular'), sg.Button('Tabela de IMC')],
        [sg.Text('', key = 'text_final')],
    ]
    return sg.Window('Calculadora de IMC', layout=layout, finalize=True)

# CRIA O LAYOUT DA JANELA 2.
def tablewin():
    sg.theme('NeonYellow1')
    layout = [
        [sg.Text('Tabela de IMC')],
        [sg.Text('Menor que 18,5 = Baixo peso')],
        [sg.Text('De 18,5 a 24,99 = Normal')],
        [sg.Text('De 25 a 29,99 = Sobrepeso')],
        [sg.Text('Maior que 30 = Obesidade')],
    ]
    return sg.Window('Tabela de IMC', layout=layout, finalize=True)

# CRIA AS JANELAS
wind1, wind2 = calcwin(), None

# CRIA UM LOOPING DE EXECUÇÃO.
while True:

    # LE TODAS AS JANELAS.
    window,event,values = sg.read_all_windows()

    # FECHA A JANELA 1.
    if window == wind1 and event == sg.WIN_CLOSED:
        break

    # ABRE A TABELA DE IMC.
    if window == wind1 and event == 'Tabela de IMC':
        if wind2 is None:
            wind2 = tablewin()
        else:
            wind2.un_hide()
    
    # CALCULA O IMC
    if window == wind1 and event == 'Calcular':
        try:
            weight = float(values['weight'])
            height = float(values['height'])
            IMC = weight / (height ** 2)
            final_result = f'Seu IMC é {IMC:.2f}'
        except ValueError:
            final_result = 'Insira Valores validos de peso e altura.'
        window['text_final'].update(final_result)

    if window == wind2 and event == sg.WIN_CLOSED:
        wind2.hide()

window.close()