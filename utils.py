def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def parse_comuna(event_input):
    """
    Function for parsing the input of comuna
    inside event
    """
    return normalize(event_input.lower())

def parse_bencina(event_input):
    """
    Function for parsing the input of bencina
    inside event
    """
    # Nota: Se agregó manejo de error si llega otro tipo
    error_message = "Error"
    possible_types = ["93", "95", "97", "diesel", "petroleo"]
    if str(event_input) in possible_types:
        return str(event_input)
    return str(error_message)

def get_top_three_fuel_prices(fuel_prices): 
    """
    Sort the fuel prices to get the top three
    args: [
        {
            "distribuidor": str,
            "direccion": str,
            "bencina": str,
            "precio": str
        }
    ]
    """
    sorted_prices = sorted(fuel_prices, key=lambda d: d["precio"])
    return sorted_prices[:3]
