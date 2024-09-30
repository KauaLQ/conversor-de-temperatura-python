def converter_temperatura(temperatura_inicial, primeira_unidade, segunda_unidade):
    try:
        temperatura_inicial = float(temperatura_inicial)
    except ValueError:
        return "Entrada inválida"

    if primeira_unidade == "Celsius(°C)" and segunda_unidade == "Kelvin(K)":
        return temperatura_inicial + 273.15
    elif primeira_unidade == "Celsius(°C)" and segunda_unidade == "Fahrenheit(°F)":
        return temperatura_inicial * (9/5) + 32
    elif primeira_unidade == "Kelvin(K)" and segunda_unidade == "Fahrenheit(°F)":
        return (temperatura_inicial - 273.15) * (9/5) + 32
    elif primeira_unidade == "Kelvin(K)" and segunda_unidade == "Celsius(°C)":
        return temperatura_inicial - 273.15
    elif primeira_unidade == "Fahrenheit(°F)" and segunda_unidade == "Celsius(°C)":
        return (temperatura_inicial - 32) * 5/9
    elif primeira_unidade == "Fahrenheit(°F)" and segunda_unidade == "Kelvin(K)":
        return (temperatura_inicial - 32) * (5/9) + 273.15

    return str(temperatura_inicial)