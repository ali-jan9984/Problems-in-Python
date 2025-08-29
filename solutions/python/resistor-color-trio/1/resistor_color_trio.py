COLORS = {"black":'0',"brown":'1',"red":'2',"orange":'3',"yellow":'4',"green":'5',"blue":'6',"violet":'7',"grey":'8',"white":'9'}


def label(colors):
    if len(colors) < 3: return 'Invalid Input.'

    try:
        first_two = COLORS[colors[0]] + COLORS[colors[1]]
        multiplier = int(COLORS[colors[2]])
    except KeyError: return 'Invalid Color'

    resistor_value = int(first_two) * (10 ** multiplier)
    
    if resistor_value >= 1000000000:
        value = resistor_value // 1000000000
        unit = 'gigaohms'
    elif resistor_value >= 1000000:
        value = resistor_value // 1000000
        unit = 'megaohms'
    elif resistor_value >= 1000:
        value = resistor_value // 1000
        unit = 'kiloohms'
    else:
        value = resistor_value
        unit = 'ohms'
    return f"{value} {unit}"

    
            
        