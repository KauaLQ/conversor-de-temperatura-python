import requests
import PySimpleGUI as sg
# link do open_weather: https://openweathermap.org/

API_KEY = "650982fb88ee01206c4ed5fe28971eb0"

def temperatura_por_coordenadas(lat, lon):
    link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br"
    response = requests.get(link)
    if response.status_code == 200:
        requisicao_dic = response.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        nome_da_cidade = requisicao_dic['name']
        return str(f"O clima em {nome_da_cidade} está {descricao}, e a temperatura é {temperatura:,.2f}ºC")
    else:
        sg.popup("Os parâmetros inseridos são inválidos. Tente novamente!")

def temperatura_por_nome(nome_cidade):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={API_KEY}&lang=pt_br"
    response = requests.get(link)
    if response.status_code == 200:
        requisicao_dic = response.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        return str(f"O clima em {nome_cidade} está {descricao}, e a temperatura é {temperatura:,.2f}ºC")
    else:
        sg.popup("Os parâmetros inseridos são inválidos. Tente novamente!")