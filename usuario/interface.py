from funcoes.conversao import converter_temperatura
from funcoes.clima import *
# Layout da janela
layout = [
    [sg.Text("O que você deseja?")],
    [sg.Combo(values=["Digitar Temperatura", "Temperatura em Tempo Real"], key="primeiraSelecao", default_value="Escolha uma opção", text_color="gray")],
    [sg.Button("Ok"), sg.Button("Cancelar")]
]

# Criando a janela
window = sg.Window("Conversor de Temperatura", layout)
segunda_opcao_adicionada = False  # Variável para controlar se a segunda parte da janela já foi adicionada
terceira_opcao_adicionada = False
# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break
    elif event == "Ok":
        opcao_escolhida = values["primeiraSelecao"]
        if opcao_escolhida == "Digitar Temperatura" and not segunda_opcao_adicionada:
            window.extend_layout(window, [[sg.Text("Digite a temperatura:", size=(15, 1)), sg.InputText(size=(12,1), key='temperatura')],
                                          [sg.Text("Unidade inicial:", size=(15, 1)), sg.Combo(values=["Celsius(°C)", "Kelvin(K)", "Fahrenheit(°F)"], key='unidade_inicial', size=(12,1))],
                                          [sg.Text("Unidade final:", size=(15, 1)), sg.Combo(values=["Celsius(°C)", "Kelvin(K)", "Fahrenheit(°F)"], key='unidade_final', size=(12,1))],
                                          [sg.Button("Converter")],
                                          [sg.Text(f"", key='resultado')]])
            segunda_opcao_adicionada = True
            window.refresh()
        elif opcao_escolhida == "Temperatura em Tempo Real" and not segunda_opcao_adicionada:
            window.extend_layout(window, [[sg.Text("Como você deseja buscar?", size=(20, 1)), sg.Radio("Por cidade", "grupo1", key='opcao1'), sg.Radio("Por coordenada", "grupo1", key='opcao2'), sg.Button("GO")],
                                          [sg.Text("", size=(21, 1), key='escolha_de_busca'), sg.InputText(size=(22, 1), key='cidade', visible=False, default_text=" ", text_color='gray'), sg.Button("Buscar", visible=False)],
                                          ])
            segunda_opcao_adicionada = True
            window.refresh()
        else:
            sg.popup("Escolha uma opção válida ou aperte\n'cancelar' para iniciar uma nova operação.")

    elif event == "Converter":
        temperatura = values['temperatura']
        unidade_inicial = values['unidade_inicial']
        unidade_final = values['unidade_final']

        resultado = converter_temperatura(temperatura, unidade_inicial, unidade_final)

        window['resultado'].update(f"A temperatura em {unidade_final} é {resultado}")

    elif event == "GO":
        if values['opcao1']:
            window['escolha_de_busca'].update("Digite o nome da cidade:")
            window['cidade'].update(visible=True)
            window['cidade'].update("Ex.: Fortaleza")
            window['Buscar'].update(visible=True)

        elif values['opcao2']:
            window['escolha_de_busca'].update("Digite as coordenadas:")
            window['cidade'].update(visible=True)
            window['cidade'].update("Ex.: -3.4105, -39.0316")
            window['Buscar'].update(visible=True)

    elif event == "Buscar":
        if values['opcao1']:
            cidade = values['cidade']
            dados = temperatura_por_nome(cidade)
            if dados != None:
                window.extend_layout(window, [[sg.Text(f"{dados}")]])
                window.refresh()
        elif values['opcao2']:
            cidade = values['cidade']
            cidade_fracionada = cidade.split(', ')
            dados_coord = temperatura_por_coordenadas(cidade_fracionada[0], cidade_fracionada[1])
            if dados_coord != None:
                window.extend_layout(window, [[sg.Text(f"{dados_coord}")]])
                window.refresh()

# Fechar a janela
window.close()