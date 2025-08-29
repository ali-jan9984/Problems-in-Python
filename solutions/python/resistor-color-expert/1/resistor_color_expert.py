COLORS = {'black':'0','brown':'1','red':'2','orange':'3','yellow':'4','green':
         '5','blue':'6','violet':'7','grey':'8','white':'9'}

TOLERANCE = {'grey':'0.05%','violet':'0.1%','blue':'0.25%','green':'0.5%','brown':'1%','red':'2%','gold':'5%','silver':'10%'}

def resistor_label(colors):
    if len(colors) < 2:
        return '0 ohms'

    tolerance = '±'+TOLERANCE[colors[-1]] 
    multiplier = 10**int(COLORS[colors[-2]])

    significant_value = colors[:-2]
    significant_integers = ''.join(COLORS[c] for c in significant_value)
    
    value_ohms = int(significant_integers) * multiplier

    if value_ohms >= 1000000000:
        value_ohms /= 1000000000
        unit = 'gigaohms'
    elif value_ohms >= 1000000:
        value_ohms /= 1000000
        unit = 'megaohms'
    elif value_ohms >= 1000:
        value_ohms /= 1000
        unit = 'kiloohms'
    else:
        unit = 'ohms'
    if value_ohms == int(value_ohms):
        value_ohms = int(value_ohms)
    return f'{value_ohms} {unit} {tolerance}'
        
        
    
    

    
    
            